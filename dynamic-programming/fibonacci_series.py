def fibonacci_sequence(n):
    # Initialize the base sequence
    sequence = [0, 1]
    
    # Handle base cases by slicing the array to the correct length
    if n == 0:
        return [sequence[0]]
    elif n == 1:
        return sequence
    
    # Generate the rest of the sequence up to index n
    for i in range(2, n + 1):
        next_num = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_num)
    
    return sequence

# Get user input
n = int(input("Enter the value of n: "))
print(f"The {n}th Fibonacci Series is: {fibonacci_sequence(n)}")
