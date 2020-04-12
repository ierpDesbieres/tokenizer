# Tokenizer

This is a minimal, configurable text tokenizer.

# Use

```python3
from tokenizer.models import Text, Token

sample = "Hello World !"
text = Text(sample)

print(text.tokens)
```