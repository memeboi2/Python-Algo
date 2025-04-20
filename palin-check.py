def is_palindrome(s):
    """Check if string is palindrome (ignoring case)"""
    s = s.lower()
    return s == s[::-1]
