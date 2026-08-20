from ..types import Ambiguity

QUANTIFIERS = {"every", "each", "all", "some", "a", "no", "any"}


def detect_scope_ambiguities(sentence: str) -> list[Ambiguity]:
    tokens = sentence.lower().split()
    quant_indices = [i for i, t in enumerate(tokens) if t in QUANTIFIERS]
    results = []

    if len(quant_indices) >= 2:
        qs = [tokens[i] for i in quant_indices]
        results.append(
            Ambiguity(
                type="scope",
                span=" ".join(qs),
                description="Multiple quantifiers may have relative scope ambiguity",
                interpretations=[
                    f"{qs[0]} has scope over {qs[1]}",
                    f"{qs[1]} has scope over {qs[0]}",
                ],
                metadata={"quantifiers": qs},
            )
        )
    return results
