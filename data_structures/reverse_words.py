def reverse_words(sentence: str) -> str:
    """
    Reverses the order of words in the sentence.

    >>> reverse_words("the sky is blue")
    'blue is sky the'
    >>> reverse_words("hello world")
    'world hello'
    """
    return ' '.join(sentence.strip().split()[::-1])
