# Metin-Ses Dönüştürme Uygulaması

[... Mevcut Türkçe içerik aynen kalacak ...]

-----------------------------------

# Text-to-Speech Conversion Application

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

- Python 3.8+
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
- GitHub: [github.com/username](https://github.com/username)
- Email: uecodengineer@gmail.com