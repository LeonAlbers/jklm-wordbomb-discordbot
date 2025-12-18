def prepare_syllable(syllable: str) -> str:
    """Prepare the syllable for searching through the wordlist."""

    syllable = syllable.lower()
    syllable = syllable.replace("ä", "a").replace("ö", "o").replace("ü", "u")

    return syllable