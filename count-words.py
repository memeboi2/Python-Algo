def count_words(text):
    """Count words in a text"""
    if not text:
        return 0
    return len(text.split())
