import math

def areaOfRings(num, isOdd):
    if not isinstance(num, int) or num <= 0:
        raise ValueError("num must be a positive integer")
    if not isinstance(isOdd, bool):
        raise ValueError("isOdd must be a boolean value (True or False)")

    total_area = 0
    for x in range(1, num + 1):
        if (isOdd and x % 2 != 0) or (not isOdd and x % 2 == 0):
            ring_area = x * x * math.pi - (x - 1) * (x - 1) * math.pi
            total_area += ring_area
    return round(total_area, 2)

# Example usage:
print(areaOfRings(5, True))  # Output: 47.12