"""
make the random hashes 
"""
import random
import redis


r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def generate_random_hash(length):
    """
    The function to generates a random hash of the given length.
    """

    hash = ""
    for i in range(length):
        hash += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    return hash

# Generate a random hash of length 10
random_hash = generate_random_hash(6)

# Print the random hash
print(random_hash)




#r.delete("test-add")


def push_hash():
    """
    The function to push 10 random hashes in the set dataset 
    """
    
    set_size = r.scard("test-add")    

    print(set_size)

    while set_size <= 9:
        random_hash = generate_random_hash(6)
        r.sadd("test-add", random_hash)
        set_size = r.scard("test-add") 

push_hash()

def print_hashes():
    """
    The function to print all hasheds 
    """
    set_members = r.smembers("test-add")

    return set_members


print(print_hashes())

print(r.scard("test-add"))