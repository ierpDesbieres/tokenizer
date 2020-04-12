import re


separators = [".", ",", ";", ".", "!", "?", ":", "'"]


class Token:
  def __init__(self, **kwargs)
    self.pos = kwargs["pos"]
    self.value = kwargs["value"]
    self.start = kwargs.get("starts")
    self.end = kwargs.get("end")
    self.isEntity = False
    self.entityType = None
    self.components = []

  def to_dict(self):
    return vars(self)

  def __str__(self):
    return self.value

  def __repr__(self):
    return f"""
    <Token pos={self.pos} value='{self.value}' start={self.start} end={self.end} >
    """

  def __len__(self):
    return len(self.value)

  @classmethod
  def hasAttr(cls, **kwargs):
    return cls(**kwargs)


class Text:
  def __init__(self, text, customTokenizer=None, seprators=separators):
    self.text = text
    self.length = len(self.text)
    self.customTokenizer = customTokenizer
    self.tokens = self.tokenize(text)

  def tokenize(self, text):
    """
    Tokenize text
    """
    if self.customTokenizer:
      tokenList = self.customTokenizer(text)
    else:
      tokenList = self.regexTokenizer(text, self.separators)
    tokenList = self.setTokenPositions(tokenList)

    tokens = [Token.addAttr(pos=pos, value=token)for pos, token in enumerate(tokenList)]
    tokens = self.setTokenPositions(tokens)

    return tokens

  def regexTokenizer(self, text, separators):
    """
    Regex tokenizer given separators
    Include spaces as tokens
    """
    sep = "".join(separators)
    pattern = re.compile(r"[\w]+|[{sep}]|\s+".format(sep=sep))
    tokenList = pattern.findall(text)

    return tokenList

  def setTokenPositions(self, tokenList):
    """
    Set token positions (must include spaces as tokens)
    """
    count = 0
    for token in tokenList:
        token.start = count
        count += len(token)
        token.end = count-1

    return tokenList

  def __str__(self):
    return str(self.text)

  def __len__(self):
    return self.length