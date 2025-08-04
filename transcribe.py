import whisper
import nltk
from nltk.tokenize import sent_tokenize

# Download tokenizer (only once; safe to keep here)
nltk.download("punkt")

# Load Whisper model
model = whisper.load_model("tiny")

def transcribe_audio(file_path):
    """
    Transcribes the given audio file and returns cleaned text.
    - Uses OpenAI Whisper Tiny model for fast inference.
    - Splits into sentences and removes very short/noisy ones.
    """
    result = model.transcribe(file_path)
    text = result["text"]

    # Break into sentences
    sentences = sent_tokenize(text)

    # Filter out very short sentences (noisy or filler speech)
    filtered = [s for s in sentences if len(s.split()) > 5]

    # Combine the cleaned transcript
    cleaned_text = " ".join(filtered)

    return cleaned_text

# Optional: Run directly for testing
if __name__ == "__main__":
    path = input("Enter the path to your audio file (.mp3 or .wav): ")
    output = transcribe_audio(path)
    print("\n🔊 Transcription Result:\n")
    print(output)
