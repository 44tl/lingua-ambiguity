from .lexical import detect_lexical_ambiguities
from .syntactic import detect_pp_attachment_ambiguities
from .scope import detect_scope_ambiguities


def detect_all(sentence: str):
    results = []
    results.extend(detect_lexical_ambiguities(sentence))
    results.extend(detect_pp_attachment_ambiguities(sentence))
    results.extend(detect_scope_ambiguities(sentence))
    return results
