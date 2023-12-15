import sys
import spacy

if 'spacy' in sys.modules:
    print("spacy is already imported")
else:
    print("spacy is not imported")

# Use spacy to load an English model and process a text
nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a sentence.")
print([token.text for token in doc])