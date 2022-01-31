"""
the file has the code for redis sorted sets
"""


#the code is not able to work for adding the elements

import redis

c = redis.Redis(host = 'localhost' , port = 6379)

#adding the items

data = "hello world"
score = 1 
c.zadd("redis_key_name", data, score)

