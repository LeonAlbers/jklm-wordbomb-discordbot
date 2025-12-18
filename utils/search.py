def find_words(words: list[str], syllable: str) -> list[str]:
    """
    Find all words in the given list that contain the specified syllable.

    Args:
        words (list[str]): A list of words to search through.
        syllable (str): The syllable to look for within the words.

    Returns:
        list[str]: A list of words that contain the specified syllable.
    """
    return [word for word in words if syllable in word]

import random

def random_word(words: list[str]) -> str:
    return random.choice(words)