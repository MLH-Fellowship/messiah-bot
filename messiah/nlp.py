import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_md")

matcher = Matcher(nlp.vocab)
offer_patterns = [
    [{"LOWER": {"IN": ["can", "could"]}}, {"LOWER": "help"}],
    [{"LOWER": {"IN": ["i'm", "am"]}},
     {"LOWER": {"IN": ["good", "experienced"]}},
     {"LOWER": {"IN": ["at", "with"]}}]
]
matcher.add("HelpOffer", offer_patterns)
request_patterns = [
    [{"LOWER": "help"}, {"LOWER": "me"}],
    [{"LOWER": "i", "OP": "?"}, {"LEMMA": "need"}, {"LOWER": "help"}],
    [{"LOWER": {"IN": ["you", "someone"]}}, {"LOWER": "help"}],
    [{"LOWER": "who"}, {"LOWER": "do"}, {"LOWER": {"IN": ["i", "you", "u"]}},
     {"LEMMA": {"IN": ["talk", "ask"]}}]
]
matcher.add("HelpRequest", request_patterns)


def get_offer_text(message_text: str):
    doc = nlp(message_text)
    for match_key, start, end in matcher(doc):
        if nlp.vocab.strings[match_key] == "HelpOffer":
            return str(doc[end:])
    return None


def get_request_text(message_text: str):
    doc = nlp(message_text)
    for match_key, start, end in matcher(doc):
        if nlp.vocab.strings[match_key] == "HelpRequest":
            return str(doc[end:])
    return None


def bio_similarity_to(question: str):
    doc = nlp(question)
    return lambda bio2: doc.similarity(nlp(bio2["bio_text"]))
