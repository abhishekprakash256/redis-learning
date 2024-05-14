"""
make the random hashes 
"""
import random


def generate_random_hash(length):
    """Generates a random hash of the given length."""

    hash = ""
    for i in range(length):
        hash += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    return hash

# Generate a random hash of length 10
random_hash = generate_random_hash(6)

# Print the random hash
print(random_hash)


