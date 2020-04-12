import re


separators = [".", ",", ";", ".", "!", "?", ":", "'"]


class Token:
    def __init__(
        self,
        pos,
        value,
        start=None,
        end=None,
        isEntity=False,
        entityType=None,
        components=[],
    ):
        self.pos = pos
        self.value = value
        self.start = start
        self.end = end
        self.isEntity = False
        self.entityType = None
        self.components = components

    def to_dict(self):
        return vars(self)

    def __str__(self):
        return self.value

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"("
            f"pos={self.pos!r},"
            f"value={self.value!r},"
            f"start={self.start!r},"
            f"end={self.end!r},"
            f"isEntity={self.isEntity!r},"
            f"entityType={self.entityType!r},"
            f"components={self.components!r},"
            f")"
        )

    def __len__(self):
        return len(self.value)

    @classmethod
    def hasAttr(cls, **kwargs):
        return cls(**kwargs)


class Text:
    def __init__(self, text, separators=separators, customTokenizer=None):
        self.text = text
        self.length = len(self.text)
        self.customTokenizer = customTokenizer
        self.separators = separators
        self.tokens = self.tokenize(text)

    def tokenize(self, text):
        """
    Tokenize text
    """
        if self.customTokenizer:
            tokenList = self.customTokenizer(text)
        else:
            tokenList = self.regexTokenizer(text, self.separators)

        tokens = [
            Token.hasAttr(pos=pos, value=token) for pos, token in enumerate(tokenList)
        ]
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
            token.end = count - 1

        return tokenList

    def __str__(self):
        return str(self.text)

    def __len__(self):
        return self.length


if __name__ == "__main__":
    token = Token(pos=1, value="Hello", start=0, end=4)
    print(eval(repr(token)))
