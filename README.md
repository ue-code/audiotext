# audiotext
 Creating a Sound Model Using Python




README.md dosyası için kapsamlı bir içerik hazırlayalım:

```markdown:README.md
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

- Python 3.8+
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
- GitHub: [github.com/kullaniciadi](https://github.com/kullaniciadi)
- E-posta: uecodengineer@email.com
```

Bu README dosyası:
1. Projenin amacını ve özelliklerini açıklıyor
2. Kurulum adımlarını detaylı olarak gösteriyor
3. Kullanım talimatlarını adım adım anlatıyor
4. Model eğitimi için gerekli bilgileri içeriyor
5. Olası hataların çözümlerini sunuyor
6. İletişim bilgilerini içeriyor

İletişim bilgilerini ve GitHub bağlantılarını kendi bilgilerinizle güncellemeyi unutmayın.
