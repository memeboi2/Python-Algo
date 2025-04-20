def remove_duplicates(items):
    """Remove duplicates while maintaining order"""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
