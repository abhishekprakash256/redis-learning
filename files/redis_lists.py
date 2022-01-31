"""
the file has the code for redis lists
"""

import redis


conn = redis.Redis(host = 'localhost' , port = 6379)

# make the list of the elememts in right push
conn.rpush('my_lst', 'random_1', 'random_2', 'random_3' , 'random_4')

# push the element in the left of the list
conn.lpush('my_lst', 'random_0')

#remove the element 
conn.lpop('my_lst')

#print the list
print(conn.lrange('my_lst' , 0 , -1))