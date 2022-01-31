"""
the file has the code for redis sorted sets
"""


import redis

c = redis.Redis(host = 'localhost' , port = 6379)

#adding the items

data = {'key_0' : 0 , 'key_1': 1}

c.zadd("redis_key_name", data)


#getting the elements
print(c.zrange('redis_key_name', 0 , -1, withscores = 'withscores'))