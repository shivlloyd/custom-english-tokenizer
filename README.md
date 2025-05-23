# English Tokenizer

A simple Python-based tokenizer for English text, inspired by ChatGPT's tiktokenizer. This basic implementation encodes individual letters (including uppercase, lowercase, and space) into numeric tokens and decodes sequences of tokens back into text.

## Features

- Simple mapping of English letters (a–z, A–Z) and space to numeric codes
- Encode text into a list of integer tokens
- Decode a list of tokens back to the original text
- Retrieve vocabulary size

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/english-tokenizer.git
   cd english-tokenizer
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

## Usage

Place your input text into the script or import the functions into your own project.

### Encoding Text

```python
from tokenizer import encode

text = "Hello World"
tokens = encode(text)
print(tokens)  # e.g. [7215121523318, 0, 8731522830]
```

### Decoding Tokens

```python
from tokenizer import decode

tokens = [7215121523318, 0, 8731522830]
original = decode(tokens)
print(original)  # "Hello World"
```

## Vocabulary

The tokenizer uses a predefined mapping (`my_vocab`) of:

- Lowercase letters `a–z` mapped to codes `11–36`
- Uppercase letters `A–Z` mapped to codes `65–90`
- Space mapped to code `0`

## Limitations

- Only supports the 52 English letters and space
- No support for punctuation, numbers, or special characters
- Tokens are generated by concatenating two-digit codes per character: contiguous runs between spaces become single integers
- Not optimized for large-scale or production use
