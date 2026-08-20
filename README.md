# lingua-ambiguity

A small toolkit that helps you find and label ambiguous bits in English sentences.  
Built for linguists, NLP tinkerers, and anyone who enjoys the quirks of language.

## What is linguistic ambiguity?

A sentence is ambiguous when it can be understood in more than one way.  
For example:

| Example sentence | Why it's ambiguous |
|------------------|--------------------|
| *She went to the bank.* | Is it a river bank or a financial bank? |
| *I saw the man with the telescope.* | Did I use the telescope, or did the man have it? |
| *Every student read a book.* | Did they all read the same book, or different ones? |

`lingua-ambiguity` spots these patterns and returns them in a clean, structured way.

## Features

- Detects **lexical**, **syntactic (PP-attachment)**, and **scope** ambiguities
- JSON output — easy to use in scripts or pipelines
- Short, human-readable explanations for each finding
- Extensible: add your own detector in a few lines of code

## Quick start

### 1. Clone the repo and set up a virtual environment

```bash
git clone https://github.com/44tl/lingua-ambiguity.git
cd lingua-ambiguity
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e .
python -m spacy download en_core_web_sm
```

### 2. Run the command-line tool

```bash
lingua-ambiguity "I saw the man with the telescope."
```

Example output:

```json
[
  {
    "type": "syntactic_attachment",
    "span": "with the telescope",
    "description": "PP can attach to verb or preceding noun",
    "interpretations": [
      "saw the man with the telescope (verb attachment)",
      "the man with the telescope (noun attachment)"
    ],
    "metadata": {
      "verb": "saw",
      "object": "man",
      "prep": "with"
    }
  }
]
```

### More examples

```bash
lingua-ambiguity "She went to the bank."
lingua-ambiguity "Every student read a book."
```

## Python API

You can also use it directly in Python:

```python
from lingua_ambiguity.detectors import detect_all

results = detect_all("I saw the man with the telescope.")

for amb in results:
    print(amb.type, "->", amb.interpretations)
```

## How it works

- **Lexical ambiguity** uses WordNet to find words with more than one meaning.
- **Syntactic ambiguity** uses spaCy to spot verb + noun + prepositional phrase patterns that could attach in two ways.
- **Scope ambiguity** flags sentences with multiple quantifiers like *every*, *a*, or *some*, where the scope is unclear.

## Contributing

Pull requests are welcome!  
Ideas for contributions:

- Add a new ambiguity detector (e.g., anaphora, ellipsis, pragmatic ambiguity)
- Improve existing heuristics
- Add example sentences or annotated data
- Build a small web UI (no need to rush this for now)
