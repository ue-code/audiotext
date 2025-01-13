from audiotext import CustomVoiceModel, read_word_file
from tkinter import Tk, filedialog
import os

def generate_speech_from_text():
    try:
        # Tkinter penceresini gizle
        root = Tk()
        root.withdraw()
        
        # Modeli yükle
        model = CustomVoiceModel("training_data")
        
        # Word dosyası seçim dialogunu göster
        print("\nLütfen Word dosyasını seçin...")
        word_file = filedialog.askopenfilename(
            title="Word Dosyası Seç",
            filetypes=[("Word Dosyaları", "*.docx"), ("Tüm Dosyalar", "*.*")]
        )
        
        if not word_file:  # Kullanıcı dosya seçmeden kapattıysa
            print("Dosya seçilmedi. Program sonlandırılıyor.")
            return
            
        try:
            # Seçilen dosyadan metni oku
            text = read_word_file(word_file)
            print("\nOkunan metin:")
            print("-" * 50)
            print(text)
            print("-" * 50)
            
            # Çıktı dosya adını otomatik oluştur
            base_name = os.path.splitext(os.path.basename(word_file))[0]
            output_file = f"{base_name}_ses.wav"
            
            # Ses sentezle
            print("\nSes dosyası oluşturuluyor...")
            model.use_trained_model(
                text=text,
                model_path='best_model.pth',
                output_file=output_file
            )
            
        except FileNotFoundError:
            print(f"Hata: {word_file} dosyası bulunamadı!")
            return
        except Exception as e:
            print(f"Dosya okuma hatası: {str(e)}")
            return
            
    except Exception as e:
        print(f"Hata oluştu: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("Ses Sentezleme Programı")
    print("=" * 30)
    generate_speech_from_text() 