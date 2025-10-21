def is_prime(num):
    """
    Checks if a given number is prime.

    A prime number is a natural number greater than 1 that has no positive divisors
    other than 1 and itself.
    """
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Check for divisibility from 2 up to the square root of the number
    # We only need to check up to the square root because if a number 'n'
    # has a divisor greater than its square root, it must also have a divisor
    # smaller than its square root.
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Found a divisor, so it's not prime
    return True  # No divisors found, so it's prime

# Example usage:
number_to_check = 17
if is_prime(number_to_check):
    print(f"{number_to_check} is a prime number.")
else:
    print(f"{number_to_check} is not a prime number.")

number_to_check = 10
if is_prime(number_to_check):
    print(f"{number_to_check} is a prime number.")
else:
    print(f"{number_to_check} is not a prime number.")
#my name is sudhanshu