"""
The file to make the hashes and store it and retrival 
check the hasing algorithm 
check the redis if hashes exist if exist make new 
"""

import redis 
import hashlib

import redis
r = redis.Redis(host='localhost', port=6379, db=0)

#make the hash 

#r.hset('test-hash','name', 'Alice')
#r.hset('test-hash','name2','Tom')

#r.delete('test-hash')

#r.hset('test-hash','name','Tom')

print(r.hget('test-hash','name').decode())
print(r.hget('test-hash','name2').decode())


#check for the existance of the hash value 


exists = r.hexists('test-hash', 'name2')
print(exists)  # Output: True (or 1)

#the hashing algorithm from python 



# Data to hash
data = b"Hello, World!"

# MD5
md5_hash = hashlib.md5(data).hexdigest()
print(f"MD5: {md5_hash}")

# SHA-1
sha1_hash = hashlib.sha1(data).hexdigest()
print(f"SHA-1: {sha1_hash}")

# SHA-256
sha256_hash = hashlib.sha256(data).hexdigest()
print(f"SHA-256: {sha256_hash}")

# BLAKE2b
blake2b_hash = hashlib.blake2b(data).hexdigest()
print(f"BLAKE2b: {blake2b_hash}")



