"""
working with hashes in redis db

"""

#code not working 

import redis
r = redis.Redis(host='localhost', port=6379, db=0)


r.hset('b', "foo", "bar", mapping={'1': 1, '2': 2})

#r.hset('a', {'1': 1, '2': 2, '3': 3})

print(r.hget('b'))


