def find_most_frequent(items):
    """Find the most frequent item in a list"""
    if not items:
        return None
    counter = {}
    for item in items:
        counter[item] = counter.get(item, 0) + 1
    
    max_count = 0
    most_frequent = items[0]
    for item, count in counter.items():
        if count > max_count:
            max_count = count
            most_frequent = item
    return most_frequent
