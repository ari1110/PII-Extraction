# Import necessary packages
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

def test_check_for_pii():
    """
    Test the check_for_pii function.
    """
    # Test case 1: No PII in the document
    document_no_pii = "This is a document without any PII."
    assert check_for_pii(document_no_pii) == []

    # Test case 2: PII present in the document
    expected_pii_matches = [
        ("Social Security Number (SSN): 123-45-6789", "PERSON"),
        ("john.doe@example.com", "EMAIL")
    ]
    assert check_for_pii(document) == expected_pii_matches

    # Test case 3: Empty document
    assert check_for_pii("") == []

    # Test case 4: Document with only non-PII entities
    document_non_pii = "I went to New York and visited the Statue of Liberty."
    assert check_for_pii(document_non_pii) == []

# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])

