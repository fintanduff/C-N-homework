def every_nth(n, p):
    if p % 2 != 0 or n > p // 2:
        raise ValueError("Invalid input: p must be even and n must be ≤ p/2")
      #This ensures that only valid numbers n and p may be used
    
    start = p // 2  # First number in range
    return list(range(start, p + 1, n))  # Generate list using range()
