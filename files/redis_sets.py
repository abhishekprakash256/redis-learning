"""
the file has the code for redis sets
"""

import redis

conn = redis.Redis(host = 'localhost' , port = 6379)

#adding the elemensts in the set

conn.sadd('my_set : set' , 'random_0' , 'random_1' , 'random_2' , 'random_3')

conn.sadd('my_set: set' , 'random_4' , 'random_5' , 'random_6' , 'random_7')

#removing the element

conn.spop('my_set: set')
conn.spop('my_set: set')
conn.spop('my_set: set')
conn.spop('my_set: set')

print(conn.smembers('my_set'))
