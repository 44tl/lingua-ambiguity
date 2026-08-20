import nltk
from nltk.corpus import wordnet as wn

from ..types import Ambiguity


def ensure_nltk_data():
    for resource_path, resource_name in [
        ("tokenizers/punkt", "punkt"),
        ("corpora/wordnet", "wordnet"),
    ]:
        try:
            nltk.data.find(resource_path)
        except LookupError:
            nltk.download(resource_name)


def detect_lexical_ambiguities(sentence: str) -> list[Ambiguity]:
    ensure_nltk_data()
    tokens = nltk.word_tokenize(sentence)
    results = []

    for token in tokens:
        if not token.isalpha():
            continue
        synsets = wn.synsets(token)
        if len(synsets) > 1:
            interpretations = [s.definition() for s in synsets[:5]]
            results.append(
                Ambiguity(
                    type="lexical",
                    span=token,
                    description=f"Word has {len(synsets)} WordNet synsets",
                    interpretations=interpretations,
                    metadata={"synset_count": len(synsets)},
                )
            )
    return results
