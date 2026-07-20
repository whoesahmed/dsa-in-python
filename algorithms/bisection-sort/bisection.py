def square_root_bisection(number, tolerance=1e-7, maximum=100):
    """Compute square root of number using bisection method.

    Args:
        number: non-negative number to compute sqrt for.
        tolerance: acceptable error in the estimated square root.
        maximum: maximum iterations.
    Returns:
        approximate square root (float) or None if did not converge.
    """
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    # Handle exact trivial cases
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    low = 0.0
    high = number if number >= 1.0 else 1.0

    for _ in range(maximum):
        mid = (low + high) / 2.0
        sq = mid * mid
        if (high - low) / 2.0 <= tolerance:
            print(f"The square root of {number} is approximately {mid}")
            return mid
        if sq < number:
            low = mid
        else:
            high = mid

    print(f"Failed to converge within {maximum} iterations")
    return None


if __name__ == '__main__':
    # Sample Examples
    examples = [0, 1, 2, 4, 9, 0.25, 12345]
    for n in examples:
        result = square_root_bisection(n)
        print(f"sqrt({n}) -> {result}\n")
