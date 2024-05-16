"""
The file to make the tiny url and combine all the pieces to work together 
inlcluding the checking of the redis and filling the set to have 10 values reserved for hashes 
"""
from redis_fun.redis_helper import *
from hashing.make_hashes import * 


#set the length of the pregenrated hashes 
PRE_GEN_HASH_NUM = 10
helper_fun = Helper_fun("url-hash","url-set")



def check_redis_set():
    """
    The function to check if the redis set has 10 unique values prebaked for hashing
    generate here and check the hash and then add in the set
    """
    len_set = redis_client.scard()
    while len_set < PRE_GEN_HASH_NUM:
        
        #genrate the new hash
        new_hash = generate_random_hash

        #check if the not exists then add
        if helper_fun.check_hash_exist(new_hash):
            helper_fun.add_value_to_set(new_hash)




def generate_tiny_url_fun(original_url):
    """
    The function to take the url and assign into the hash value 
    put the new value for the mapping from the flask server 
    """
    
    new_url = helper_fun.pop_set_val()
    check_redis_status()

    #add the url in the redis with new hash value
    helper_fun.add_value_to_hash(original_url,new_url)



