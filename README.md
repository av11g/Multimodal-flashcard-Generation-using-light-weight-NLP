#  Auto Flashcard Generator

A lightweight AI-powered web application that automatically generates flashcards from **audio lectures**, **PDF documents**, and **PowerPoint slides**. Ideal for students, educators, and self-learners to enhance their learning experience using quick revision cards.

---

##  Overview

In the era of digital learning, students are often overwhelmed by long lectures and extensive study materials. This tool bridges the gap between **passive content consumption** and **active recall** by converting lecture data into concise, easy-to-understand flashcards using NLP.

---

##  Features

- 🎙️ Upload **audio files** (`.mp3`, `.wav`) and get transcripted content using Whisper.
- 📄 Upload **PDFs or PPTX slides**, and extract key points and text.
- 🤖 Generate flashcards using lightweight **spaCy NLP** techniques.
- 📥 Download flashcards in **CSV format** for use in apps like Anki, Quizlet, etc.
- 💡 Interactive flashcard interface (click to reveal answer).
- 🖥️ Works as a web application using **Streamlit**.
- 📦 Low resource usage – suitable for browser or mobile.

---

##  Demo

> Coming soon: [Deployed App Link]

---

## 🛠️ Tech Stack

| Area              | Tools / Libraries                          |
|-------------------|--------------------------------------------|
| Backend           | Python 3.x                                 |
| Web Framework     | Streamlit                                  |
| Audio Transcription | OpenAI Whisper                           |
| NLP               | spaCy (`en_core_web_sm`), NLTK             |
| File Handling     | python-pptx, PyMuPDF (fitz)                |
| Output Format     | CSV                                        |
| Deployment        | Streamlit Cloud / Render / Heroku          |

---

## 📁 Folder Structure
├── app.py # Main Streamlit app
├── transcribe.py # Audio-to-text logic (Whisper)
├── slide_text_extractor.py # PDF & PPT text extraction
├── transcript_flashcards.py # Flashcard generator
├── templates/ # HTML templates (if extended)
│ ├── index.html
│ └── result.html
├── requirements.txt # Python dependencies
└── README.md # You're here

