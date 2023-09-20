import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import pyttsx3
import speech_recognition as sr

def convert_voice_to_text(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        try:
            audio = recognizer.record(source)
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Couldn't understand the audio."
        except sr.RequestError:
            return "Couldn't request results; check your network connection."

def process_voice_note():
    if not os.path.exists("voice_notes"):
        os.makedirs("voice_notes")

    audio_file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])

    if not os.path.isfile(audio_file_path):
        messagebox.showerror("Error", "File not found. Please provide a valid file path.")
        return

    text = convert_voice_to_text(audio_file_path)
    
    text_output.config(state=tk.NORMAL)
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, text)
    text_output.config(state=tk.DISABLED)

def speak_text():
    text = text_output.get(1.0, tk.END)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Create the main window
root = tk.Tk()
root.title("WhatsApp Voice Note to Text Converter")
root.geometry("400x300")

# Create GUI elements
title_label = tk.Label(root, text="WhatsApp Voice Note to Text Converter", font=("Arial", 14))
process_button = tk.Button(root, text="Process Voice Note", command=process_voice_note)
speak_button = tk.Button(root, text="Speak Text", command=speak_text)
text_output = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED)

# Place GUI elements
title_label.pack(pady=10)
process_button.pack(pady=10)
speak_button.pack(pady=10)
text_output.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Start the GUI main loop
root.mainloop()
