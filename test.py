from extractor import extract_txt
from gemini_client import get_summary, get_flashcards, get_definitions
from utils import chunk_text


PDF_PATH = "test.pdf"  
LANGUAGE = "English"


print("=== LUMI SMOKE TEST ===\n")


print("Step 1: Extracting text...")
raw_text = extract_txt(PDF_PATH)
text = chunk_text(raw_text)
print(f"Extracted {len(raw_text)} characters, using first {len(text)} chars\n")


print("Step 2: Generating summary...")
summary = get_summary(text, LANGUAGE)
print("SUMMARY:")
print(summary)
print()


print("Step 3: Generating flashcards...")
flashcards = get_flashcards(text, LANGUAGE)
print(f"FLASHCARDS ({len(flashcards)} generated):")
for i, card in enumerate(flashcards, 1):
    print(f"  {i}. Q: {card['question']}")
    print(f"     A: {card['answer']}")
print()


print("Step 4: Generating definitions...")
definitions = get_definitions(text, LANGUAGE)
print(f"DEFINITIONS ({len(definitions)} generated):")
for item in definitions:
    print(f"  - {item['term']}: {item['definition']}")
print()

print("=== SMOKE TEST COMPLETE ===")
