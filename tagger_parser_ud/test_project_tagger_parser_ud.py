import pytest
import spacy
from spacy.lang.en import English
from spacy.tokens import Doc
from spacy.training import Example
from spacy.util import compile_infix_regex
from spacy.pipeline import Tagger, DependencyParser
from spacy.tokens import Token
import random
from spacy.util import minibatch
from spacy.training import Example
from spacy.util import compile_prefix_regex, compile_infix_regex, compile_suffix_regex
from spacy.scorer import Scorer
from spacy.training import iob_to_biluo
from spacy.training import validate_examples, validate_get_examples
from pathlib import Path
from spacy.lang.en import English
from spacy.scorer import Scorer


def test_taggerparser_ud_project():
    nlp = spacy.load("en_core_web_sm")
    # nlp = spacy.blank("en")  # or load a different language if you're not working with English
    tagger = nlp.add_pipe("tagger")
    parser = nlp.add_pipe("parser")

    # Create some Example objects with the correct annotations
    examples = []
    scorer = Scorer(nlp.vocab)

    for _ in range(100):  # replace with your actual data
        doc = Doc(nlp.vocab, words=["This", "is", "a", "sentence", "."])
        example = Example.from_dict(doc, {"tags": ["DET", "VERB", "DET", "NOUN", "PUNCT"]})
        examples.append(example)

    tagger.initialize(lambda: examples, nlp=nlp)
    parser.initialize(lambda: examples, nlp=nlp)

    # Train the tagger and parser
    for epoch in range(10):  # replace with your actual number of epochs
        random.shuffle(examples)
        for batch in minibatch(examples, size=8):  # replace with your actual batch size
            tagger.update(batch)
            parser.update(batch)

    # # Evaluate the tagger and parser
    # scorer = Scorer(nlp.vocab)
    # for example in examples:
    #     pred_doc = nlp(example.text)
    #     gold_doc = example.reference
    #     example = Example(pred_doc, gold_doc)
    #     scorer.score(example)
    # print(scorer.scores)

    # Evaluate the tagger and parser
    scorer = Scorer(nlp.vocab)
    for example in examples:
        words = example.text.split() #split the text into words
        pred_doc = Doc(nlp.vocab, words=words)
        tagger(pred_doc)    # tagger is not a component of the pipeline
        parser(pred_doc)    # parser is not a component of the pipeline
        example = Example(pred_doc, example.reference)
        scorer.score(example)
    print(scorer.scores)

test_taggerparser_ud_project()