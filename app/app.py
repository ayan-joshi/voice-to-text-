from flask import Flask, render_template, request
import os
import main  # Import your existing Python code

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        audio_file = request.files['audio']
        if audio_file and audio_file.filename.endswith(('.wav', '.mp3')):
            audio_file_path = os.path.join('uploads', audio_file.filename)
            audio_file.save(audio_file_path)
            result = main.convert_voice_to_text(audio_file_path)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
