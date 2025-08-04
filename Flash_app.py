import os
from flask import Flask, render_template, request
from transcribe import transcribe_audio
from slide_text_extractor import extract_slide_text
from Transcript_flashcards import generate_flashcards

# Create uploads folder if not exists
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        audio_file = request.files.get("audio_file")
        slide_file = request.files.get("slide_file")

        audio_text = ""
        slide_text = ""

        # Save and process audio file
        if audio_file and audio_file.filename.endswith(".mp3"):
            audio_path = os.path.join(app.config["UPLOAD_FOLDER"], audio_file.filename)
            audio_file.save(audio_path)
            audio_text = transcribe_audio(audio_path)

        # Save and process slide or PDF file
        if slide_file and (slide_file.filename.endswith(".pptx") or slide_file.filename.endswith(".pdf")):
            slide_path = os.path.join(app.config["UPLOAD_FOLDER"], slide_file.filename)
            slide_file.save(slide_path)
            slide_text = extract_slide_text(slide_path)

        # Combine and process
        combined_text = audio_text + "\n" + slide_text
        flashcards = generate_flashcards(combined_text)

        return render_template("result.html", flashcards=flashcards)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
