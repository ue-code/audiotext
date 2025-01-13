# audiotext
Metin-Ses Dönüştürme Uygulaması / Creating a Sound Model Using Python

# Metin-Ses Dönüştürme Uygulaması

Bu proje, Word belgelerindeki metinleri ses dosyalarına dönüştüren bir Python uygulamasıdır. Facebook'un Türkçe dil modelini (facebook/mms-tts-tur) kullanarak metinleri doğal bir ses tonuyla seslendirmektedir.

## Özellikler

- Word (.docx) belgelerinden metin okuma
- Türkçe metinleri sese dönüştürme
- Özelleştirilebilir ses modeli eğitimi
- Kolay kullanımlı görsel arayüz
- Otomatik dosya adlandırma

## Kurulum

1. Gerekli Python paketlerini yükleyin:
```bash
pip install torch torchvision torchaudio
pip install transformers
pip install python-docx
pip install numpy
pip install scipy
pip install soundfile
```

2. Projeyi klonlayın:
```bash
git clone https://github.com/kullaniciadi/metin-ses-donusturucu.git
cd metin-ses-donusturucu
```

## Kullanım

1. Programı çalıştırın:
```bash
python generate_speech.py
```

2. Açılan dosya seçim penceresinden bir Word belgesi seçin
3. Program otomatik olarak:
   - Metni Word belgesinden okuyacak
   - Okunan metni ekranda gösterecek
   - Ses dosyasını oluşturacak

Çıktı dosyası, Word belgesinin adıyla aynı dizinde "_ses.wav" uzantısıyla oluşturulacaktır.

## Model Eğitimi (İsteğe Bağlı)

Kendi ses modelinizi eğitmek için:

1. `training_data` klasörü oluşturun
2. Ses kayıtlarını (.wav) ve transkriptleri (.txt) ekleyin:
```
training_data/
    ├── konusma1.wav
    ├── konusma1.txt
    ├── konusma2.wav
    ├── konusma2.txt
    └── ...
```
3. Model eğitimini başlatın:
```bash
python audiotext.py
```

## Dosya Yapısı

- `generate_speech.py`: Ana program dosyası
- `audiotext.py`: Model ve ses işleme fonksiyonları
- `training_data/`: Eğitim verileri klasörü
- `best_model.pth`: Eğitilmiş model dosyası

## Gereksinimler

- Python 3.9
- PyTorch
- Transformers
- python-docx
- numpy
- scipy
- soundfile

## Notlar

- Word belgesinin UTF-8 formatında kaydedilmiş olması önerilir
- Ses çıktısı 22050 Hz örnekleme hızında oluşturulur
- Model eğitimi için GPU önerilir

## Hata Çözümleri

1. "Model bulunamadı" hatası:
   - `best_model.pth` dosyasının proje dizininde olduğundan emin olun
   
2. Word dosyası okunamıyor:
   - Dosyanın .docx formatında olduğunu kontrol edin
   - Dosya izinlerini kontrol edin

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## İletişim

Sorularınız ve önerileriniz için:
- E-posta: uecodengineer@gmail.com
```

## audiotext

Metin-Ses Dönüştürme Uygulaması / Creating a Sound Model Using Python

## Creating a Sound Model Using Python

This project is a Python application that converts text from Word documents into audio files. It uses Facebook's Turkish language model (facebook/mms-tts-tur) to vocalize texts with a natural tone.

## Features

- Text reading from Word (.docx) documents
- Text-to-speech conversion for Turkish texts
- Customizable voice model training
- User-friendly visual interface
- Automatic file naming

## Installation

1. Install required Python packages:
```bash
pip install torch torchvision torchaudio
pip install transformers
pip install python-docx
pip install numpy
pip install scipy
pip install soundfile
```

2. Clone the project:
```bash
git clone https://github.com/username/text-to-speech-converter.git
cd text-to-speech-converter
```

## Usage

1. Run the program:
```bash
python generate_speech.py
```

2. Select a Word document from the file selection window
3. The program will automatically:
   - Read the text from the Word document
   - Display the read text
   - Generate the audio file

The output file will be created in the same directory as the Word document with "_ses.wav" extension.

## Model Training (Optional)

To train your own voice model:

1. Create a `training_data` folder
2. Add voice recordings (.wav) and transcripts (.txt):
```
training_data/
    ├── speech1.wav
    ├── speech1.txt
    ├── speech2.wav
    ├── speech2.txt
    └── ...
```
3. Start model training:
```bash
python audiotext.py
```

## File Structure

- `generate_speech.py`: Main program file
- `audiotext.py`: Model and audio processing functions
- `training_data/`: Training data folder
- `best_model.pth`: Trained model file

## Requirements

- Python 3.9
- PyTorch
- Transformers
- python-docx
- numpy
- scipy
- soundfile

## Notes

- Word document should be saved in UTF-8 format
- Audio output is generated at 22050 Hz sampling rate
- GPU is recommended for model training

## Troubleshooting

1. "Model not found" error:
   - Ensure `best_model.pth` file exists in the project directory
   
2. Word document cannot be read:
   - Check if the file is in .docx format
   - Check file permissions

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions and suggestions:
- Email: uecodengineer@gmail.com
