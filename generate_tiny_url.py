"""
The file to make the tiny url and combine all the pieces to work together 
inlcluding the checking of the redis and filling the set to have 10 values reserved for hashes 
"""
from redis_fun.redis_helper import *
from hashing.make_hashes import * 



def check_redis_set():
    """
    The function to check if the redis set has 10 unique values prebaked for hashing
    """

    pass



def generate_tiny_url_fun():
    """
    The function to take the url and assign into the hash value 
    put the new value for the mapping from the flask server 
    """
    pass
