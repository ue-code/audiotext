from gtts import gTTS
import json
from docx import Document
import os
import torch
import numpy as np
from scipy.io.wavfile import write
from transformers import VitsModel, AutoProcessor
from datasets import load_dataset
import traceback

def read_word_file(file_path):
    """Word belgesinden metni okur"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dosya bulunamadı: {file_path}")
        
    doc = Document(file_path)
    full_text = []
    for paragraph in doc.paragraphs:
        if paragraph.text.strip() != "":  # Boş paragrafları atla
            full_text.append(paragraph.text)
    return " ".join(full_text)

class CustomVoiceModel:
    def __init__(self, training_audio_dir):
        self.training_audio_dir = training_audio_dir
        self.model = None
        self.processor = None

    def prepare_training_data(self):
        """Eğitim verilerini hazırla"""
        audio_files = []
        transcripts = []
        
        try:
            for file in os.listdir(self.training_audio_dir):
                if file.endswith('.wav'):
                    audio_path = os.path.join(self.training_audio_dir, file)
                    
                    # Ses dosyasının özelliklerini kontrol et
                    import soundfile as sf
                    audio_data, sample_rate = sf.read(audio_path)
                    print(f"Ses dosyası: {file}")
                    print(f"Örnekleme hızı: {sample_rate} Hz")
                    print(f"Kanal sayısı: {audio_data.shape[1] if len(audio_data.shape) > 1 else 1}")
                    print(f"Süre: {len(audio_data)/sample_rate:.2f} saniye")
                    print("-" * 50)
                    
                    # Ses dosyasını numpy array'e dönüştür ve kaydet
                    audio_np_path = os.path.splitext(audio_path)[0] + '.npy'
                    
                    if not os.path.exists(audio_np_path):
                        # Ses verisini tek kanallı hale getir
                        if len(audio_data) > 1:
                            audio_data = audio_data.mean(axis=1)
                        
                        # Sabit uzunluğa getir (48896 örnek)
                        target_length = 48896
                        if len(audio_data) > target_length:
                            audio_data = audio_data[:target_length]
                        elif len(audio_data) < target_length:
                            # Eksik kısmı sıfırlarla doldur
                            padding = np.zeros(target_length - len(audio_data))
                            audio_data = np.concatenate([audio_data, padding])
                        
                        np.save(audio_np_path, audio_data)
                    
                    audio_files.append(audio_np_path)
                    
                    # Transkript dosyasını oku
                    transcript_file = os.path.splitext(file)[0] + '.txt'
                    with open(os.path.join(self.training_audio_dir, transcript_file), 'r', encoding='utf-8') as f:
                        transcripts.append(f.read().strip())
            
            return audio_files, transcripts
            
        except Exception as e:
            print(f"Veri hazırlama sırasında hata oluştu: {str(e)}")
            raise e

    def train_model(self, epochs=100):
        """Modeli eğit"""
        try:
            # Model ve işlemciyi yükle
            self.model = VitsModel.from_pretrained("facebook/mms-tts-tur")
            self.processor = AutoProcessor.from_pretrained("facebook/mms-tts-tur")
            
            # Eğitim verilerini hazırla
            audio_files, transcripts = self.prepare_training_data()
            
            # Eğitim döngüsü
            self.model.train()
            optimizer = torch.optim.Adam(self.model.parameters(), lr=0.0001)  # Öğrenme oranını düşürdük
            scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'min', patience=5)
            
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            self.model.to(device)
            
            best_loss = float('inf')
            
            for epoch in range(epochs):
                total_loss = 0
                for audio_file, transcript in zip(audio_files, transcripts):
                    # Ses ve metin verilerini işle
                    inputs = self.processor(text=transcript, return_tensors="pt")
                    inputs = {k: v.to(device) for k, v in inputs.items()}
                    
                    # Forward pass
                    outputs = self.model(**inputs)
                    
                    # MSE loss hesapla
                    target_audio = torch.from_numpy(np.load(audio_file)).float()
                    target_audio = target_audio.to(device)
                    
                    # Ses verilerini yeniden şekillendir
                    predicted_audio = outputs.waveform[0].squeeze()  # Batch boyutunu kaldır
                    if len(predicted_audio.shape) == 1:
                        predicted_audio = predicted_audio.unsqueeze(-1)
                    if len(target_audio.shape) == 1:
                        target_audio = target_audio.unsqueeze(-1)
                    
                    # Boyutları eşitle
                    min_length = min(predicted_audio.shape[0], target_audio.shape[0])
                    predicted_audio = predicted_audio[:min_length]
                    target_audio = target_audio[:min_length]
                    
                    # Kanal sayısını kontrol et
                    if predicted_audio.shape[-1] != target_audio.shape[-1]:
                        if predicted_audio.shape[-1] == 1:
                            predicted_audio = predicted_audio.expand(-1, target_audio.shape[-1])
                        elif target_audio.shape[-1] == 1:
                            target_audio = target_audio.expand(-1, predicted_audio.shape[-1])
                    
                    loss = torch.nn.functional.mse_loss(predicted_audio, target_audio)
                    
                    # Backward pass
                    optimizer.zero_grad()
                    loss.backward()
                    optimizer.step()
                    
                    total_loss += loss.item()
                    
                avg_loss = total_loss / len(audio_files)
                print(f"Epoch {epoch+1}/{epochs}, Average Loss: {avg_loss:.4f}")
                
                # Learning rate'i güncelle
                scheduler.step(avg_loss)
                
                # En iyi modeli kaydet
                if avg_loss < best_loss:
                    best_loss = avg_loss
                    torch.save(self.model.state_dict(), 'best_model.pth')
                    
                # Her 10 epoch'ta bir test çıktısı al
                if (epoch + 1) % 10 == 0:
                    test_text = "Bu bir ara test cümlesidir."
                    self.generate_speech(test_text, f"test_epoch_{epoch+1}.wav")
                    
        except Exception as e:
            print(f"Model eğitimi sırasında hata oluştu: {str(e)}")
            raise e

    def generate_speech(self, text, output_file="custom_output.wav"):
        """Metni kişiselleştirilmiş ses ile sentezle"""
        if self.model is None:
            raise ValueError("Model henüz eğitilmemiş!")
            
        inputs = self.processor(text=text, return_tensors="pt")
        with torch.no_grad():
            output = self.model(**inputs)
        
        # Ses dalgasını kaydet
        write(output_file, 22050, output.waveform[0].numpy())

    def use_trained_model(self, text, model_path='best_model.pth', output_file="output.wav"):
        """Eğitilmiş modeli kullanarak yeni metin üzerinde ses sentezi yap"""
        try:
            # Model ve işlemciyi yükle (eğer yüklü değilse)
            if self.model is None:
                self.model = VitsModel.from_pretrained("facebook/mms-tts-tur")
                self.processor = AutoProcessor.from_pretrained("facebook/mms-tts-tur")
                
                # Eğitilmiş model parametrelerini yükle
                if os.path.exists(model_path):
                    self.model.load_state_dict(torch.load(model_path))
                    print(f"Model yüklendi: {model_path}")
                else:
                    print("Uyarı: Eğitilmiş model bulunamadı, varsayılan model kullanılıyor.")
            
            # Modeli değerlendirme moduna al
            self.model.eval()
            
            # Metni ses dalgasına dönüştür
            inputs = self.processor(text=text, return_tensors="pt")
            with torch.no_grad():
                output = self.model(**inputs)
            
            # Ses dalgasını kaydet
            write(output_file, 22050, output.waveform[0].numpy())
            print(f"Ses dosyası oluşturuldu: {output_file}")
            
        except Exception as e:
            print(f"Ses sentezi sırasında hata oluştu: {str(e)}")
            raise e

# Kullanım örneği
def main():
    try:
        # Eğitilmiş modeli kullanma örneği
        model = CustomVoiceModel("training_data")
        
        # Yeni bir metin üzerinde dene
        test_text = "Bu metin, eğitilmiş model tarafından sese dönüştürülecek."
        model.use_trained_model(
            text=test_text,
            model_path='best_model.pth',  # Eğitim sırasında kaydedilen en iyi model
            output_file="yeni_cikti.wav"
        )
        
    except Exception as e:
        print(f"Hata oluştu: {str(e)}")
        traceback.print_exc()

if __name__ == "__main__":
    main()