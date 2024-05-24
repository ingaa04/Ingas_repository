def largest_prime_factor(n):
        # Initialize the largest prime factor
    largest_factor = 1

        # Divide by 2 until it's no longer divisible
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

        # Check odd numbers starting from 3
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            largest_factor = i
            n //= i

        # If n is still greater than 2, it's a prime factor
    if n > 2:
        largest_factor = n

    print(largest_factor)
    return largest_factor

largest_prime_factor(1140)