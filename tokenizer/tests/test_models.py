import pytest

from ..models import Token, Text 

SAMPLE_TEXT = "Hello, World !"
SAMPLE_FIRST_TOKENS = {
    "pos": 0,
    "value": "Hello",
    "start": 0,
    "end": 4,
    "components": []
  }

SAMPLE_TOKENS = {
    "pos": 0,
    "value": "Hello",
    "start": 0,
    "end": 4,
    "components": []
  }


EXPECTED_TOKEN = Token(**SAMPLE_FIRST_TOKENS)
def test_Text():
  text = Text(SAMPLE_TEXT)
  first_token = text.tokens[0]

  assert len(text) == len(SAMPLE_TEXT)
  assert first_token.to_dict() == EXPECTED_TOKEN.to_dict()
  assert str(first_token) == str(EXPECTED_TOKEN)
  assert len(first_token) == len(EXPECTED_TOKEN)
  assert len(text) == 14