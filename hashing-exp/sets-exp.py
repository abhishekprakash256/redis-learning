"""
redis deal with the sets 
"""

import redis 
import hashlib

import redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)


#r.sadd("test-add", "first")
#r.sadd("test-add", "second")

popped_item = r.spop("test-add")

print(popped_item)


