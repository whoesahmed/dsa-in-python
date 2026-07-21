def verify_card_number(card_number: str) -> str:
    """Verify a card number string using the Luhn algorithm.

    Strips spaces and dashes. Returns 'VALID!' if the number passes Luhn, else 'INVALID!'.
    """
    # Remove spaces and dashes
    s = ''.join(ch for ch in card_number if ch.isdigit())
    if not s:
        return 'INVALID!'

    # Luhn algorithm: starting from the rightmost digit (check digit), moving left,
    # double every second digit (i.e., digits in even positions from the right, 0-based)
    total = 0
    reverse_digits = s[::-1]
    for i, ch in enumerate(reverse_digits):
        d = int(ch)
        if i % 2 == 1:
            d = d * 2
            if d > 9:
                d -= 9
        total += d

    return 'VALID!' if total % 10 == 0 else 'INVALID!'


if __name__ == '__main__':
    # quick manual checks
    samples = [
        '453914889',
        '4111-1111-1111-1111',
        '453914881',
        '1234 5678 9012 3456',
    ]
    for s in samples:
        print(s, verify_card_number(s))
