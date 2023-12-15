# Import necessary packages
import re
import spacy
import pytest

# Load the language model
nlp = spacy.load("en_core_web_sm")

# Define a function to check for PII
def check_for_pii(text):
    # Tokenize the text using spaCy
    doc = nlp(text)

    # Check for PII patterns in the text
    pii_matches = []

    # Use spaCy's Named Entity Recognition to find entities
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "ORG", "GPE", "EMAIL", "PHONE"]:
            pii_matches.append((ent.text, ent.label_))

    # Return the found PII matches
    return pii_matches

# Example usage
document = """
This is an example document that contains some PII such as:
- Social Security Number (SSN): 123-45-6789
- Email address: john.doe@example.com
"""

pii_matches = check_for_pii(document)
print("Found PII matches:")
for pii in pii_matches:
    print(pii)
