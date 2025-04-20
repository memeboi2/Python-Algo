def mod_pow(base, exponent, modulus):
    """
    Calculate (base^exponent) % modulus efficiently using binary exponentiation
    This is more efficient than pow(base, exponent) % modulus for large numbers
    """
    if modulus == 1:
        return 0
    
    result = 1
    base = base % modulus
    
    while exponent > 0:
        # If exponent is odd, multiply result with base
        if exponent % 2 == 1:
            result = (result * base) % modulus
        
        # Exponent is even, square the base
        exponent = exponent >> 1  # Equivalent to exponent //= 2
        base = (base * base) % modulus
    
    return result
