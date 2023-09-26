# Voice to Text Converter App

This Python application allows you to convert voice recordings into text. You can also have the converted text spoken aloud.

## Prerequisites

Before running the application, make sure you have the following libraries installed:

- tkinter: for the graphical user interface (GUI)
- pyttsx3: for text-to-speech conversion
- speech_recognition: for voice recognition

You can install these libraries using pip:

```bash
pip install tkinter pyttsx3 SpeechRecognition
```

## Usage

1. Run the application by executing the Python script.

```bash
python voice_to_text_converter.py
```

2. The application's main window will appear.

3. Click the "Process Voice Note" button to select an audio file (supported formats: .wav and .mp3) containing the voice recording you want to convert to text.

4. After processing, the converted text will appear in the text box.

5. Click the "Speak Text" button to have the converted text spoken aloud.

## Notes

- If the "voice_notes" directory doesn't exist in the application's folder, it will be created automatically to store processed voice notes.

- If the application encounters any issues while processing audio or requesting results, it will display an appropriate error message.

- You can replace the font and customize the graphical elements of the GUI according to your preferences by modifying the code.

## Important

- This application requires an active internet connection to use the Google Web Speech API for voice recognition.

- The accuracy of voice recognition may vary depending on the quality of the audio recording and the clarity of the spoken words.

- Make sure to provide valid file paths for audio files when using the "Process Voice Note" feature.

Feel free to explore and enhance the functionality of this Voice to Text Converter app according to your needs. Happy coding!

