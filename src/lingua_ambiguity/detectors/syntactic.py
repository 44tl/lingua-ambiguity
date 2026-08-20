import spacy

from ..types import Ambiguity

_nlp = None


def get_nlp():
    global _nlp
    if _nlp is None:
        _nlp = spacy.load("en_core_web_sm")
    return _nlp


def detect_pp_attachment_ambiguities(sentence: str) -> list[Ambiguity]:
    nlp = get_nlp()
    doc = nlp(sentence)
    results = []

    for token in doc:
        if token.pos_ == "ADP" and token.head.pos_ == "VERB":
            for child in token.head.children:
                if child.dep_ in ("dobj", "obj") and child.i < token.i:
                    pp_span = " ".join(t.text for t in token.subtree)
                    results.append(
                        Ambiguity(
                            type="syntactic_attachment",
                            span=pp_span,
                            description="PP can attach to verb or preceding noun",
                            interpretations=[
                                f"{token.head.text} {child.text} {pp_span} (verb attachment)",
                                f"{child.text} {pp_span} (noun attachment)",
                            ],
                            metadata={
                                "verb": token.head.text,
                                "object": child.text,
                                "prep": token.text,
                            },
                        )
                    )
    return results
