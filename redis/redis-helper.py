"""
The redis helper function to add the connection and methods to add the data 
"""

#imports 
import redis
import os 


def check_redis_status():
    try:
        # Execute the command to check MongoDB server status
        result = os.system("redis-cli 'ping'")
        
        # Check if the command was successful
        if result == 0:
            print("Redis is installed and running.")
            return True
        else:
            print("Redis is not installed or not running.")
            return False
    
    except FileNotFoundError:
        # Handle the case where 'mongod' command is not found (MongoDB not installed)
        print("Redis is not installed.")
        return False



#create the database client 
def create_redis_client():


    redis_status = check_redis_status()

    if redis_status:
        try:

            # Attempt to create a MongoClient
            client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
            print("Redis client created successfully.")
            return client

        except ImportError:
            # Print error message if pymongo is not installed
            print("Redsi is not installed on this system.")
            return None

        except Exception as e:
            # Print error message if MongoClient creation fails for other reasons
            print("Error creating Redis client:", e)
            return None
    
    else:
        return "Redis Missing"



redis_client = create_redis_client()

class Helper_fun():

    def __init__(self,hash_name, set_name):
        self.hash_name = hash_name
        self.set_name = set_name

    def add_value_to_set(value):
        """
        The function to add value to the set 
        """
        #add the value to the set 

        res = redis_client.sadd(self.set_name, set_name)

        if res: 
            print("Data added in set succesfully")
        
        else:
            print("Failed to add data in set")
    
    
    def add_value_to_hash(key , value):
        """
        The function to add value to the set 
        """
        #add the value to the set 

        res = redis_client.hset(self.hash_name,key, value)

        if res: 
            print("Data added in set succesfully")
        
        else:
            print("Failed to add data in set")

    
    def delete_db(db_name):
        """
        The function to delete the hash if exists 
        and then delete the hash
        """
        # check the hash exists 
        if redis_client.exists(db_name):
            
            #delete the hash
            redis_client.delete(db_name)
            print("value added succesfully")
        
        else:

            print("The db doesn't exists")

    
    def pop_set_val():
        """
        The funcion to pop a value from the set 
        """

        return redis_client.spop(self.set_name)
    
    
    def get_hash_value(hash_val):
        """
        The function to get the hash value 
        """
        return redis_client.hget(self.hash_name, hash_val)

    def check_hash_exist(hash_val):
        """
        The function to check the hash value exist in the set and in the redis hash
        """

        hash_check = redis_client.hexists(self.hash_name, hash_val)
        
        if hash_check:
            return True 
        
        else:
            return False





print(redis_client.exists('test-hash'))

    




        



