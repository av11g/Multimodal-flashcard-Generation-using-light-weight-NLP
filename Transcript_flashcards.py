import spacy

# Load lightweight spaCy model
nlp = spacy.load("en_core_web_sm")

def generate_flashcards(text):
    doc = nlp(text)
    flashcards = []
    used_phrases = set()

    for sent in doc.sents:
        for chunk in sent.noun_chunks:
            phrase = chunk.text.strip()

            if len(phrase.split()) < 2 or phrase.lower() in used_phrases:
                continue

            used_phrases.add(phrase.lower())

            question = f"What is {phrase}?"
            answer = sent.text.strip()
            flashcards.append((question, answer))
            break  # One flashcard per sentence

    return flashcards
