import streamlit as st
import os
import tempfile
from transcribe import transcribe_audio  # Your audio transcription logic
from slide_text_extractor import extract_slide_text  # Your slide/pdf extractor
from Transcript_flashcards import generate_flashcards  # Your flashcard generator
import csv
import io

# Title
st.set_page_config(page_title="Auto Flashcard Generator", layout="centered")
st.title("📚 Auto Flashcard Generator")
st.write("Upload your audio, PPT, or PDF to auto-generate flashcards.")

# File upload
uploaded_audio = st.file_uploader("🎙️ Upload an audio file (.mp3 or .wav)", type=["mp3", "wav"])
uploaded_doc = st.file_uploader("📄 Upload a slide or document (.pptx or .pdf)", type=["pptx", "pdf"])

# Submit button
if st.button("🚀 Generate Flashcards"):
    if not uploaded_audio and not uploaded_doc:
        st.warning("⚠️ Please upload at least one file.")
    else:
        full_text = ""

        # Handle audio transcription
        if uploaded_audio:
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_audio.name)[1]) as tmp_audio:
                tmp_audio.write(uploaded_audio.read())
                audio_path = tmp_audio.name
            st.info("📝 Transcribing audio...")
            full_text += transcribe_audio(audio_path) + "\n"

        # Handle slide/pdf extraction
        if uploaded_doc:
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_doc.name)[1]) as tmp_doc:
                tmp_doc.write(uploaded_doc.read())
                doc_path = tmp_doc.name
            st.info("📄 Extracting text from PPT/PDF...")
            full_text += extract_slide_text(doc_path)

        # Generate flashcards
        st.info("🧠 Generating flashcards...")
        flashcards = generate_flashcards(full_text)

        # Display flashcards using expanders
        if flashcards:
            st.success("✅ Flashcards generated! Click each question to reveal the answer.")
            for i, (q, a) in enumerate(flashcards, 1):
                with st.expander(f"Q{i}: {q}"):
                    st.markdown(f"**Answer:** {a}")

            # Offer CSV download
            csv_buffer = io.StringIO()
            writer = csv.writer(csv_buffer)
            writer.writerow(["Question", "Answer"])
            writer.writerows(flashcards)
            st.download_button(
                label="📥 Download Flashcards as CSV",
                data=csv_buffer.getvalue(),
                file_name="flashcards.csv",
                mime="text/csv"
            )
        else:
            st.warning("⚠️ No flashcards could be generated.")
