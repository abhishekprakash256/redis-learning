## Redis 

### installation  

```sh
sudo apt update
sudo apt install redis-server
```

### Commands

- Start 

  ```sh
  redis-server (to start service)
  sudo service redis-server start
  ```

- Restart

  ```sh
  sudo systemctl restart redis-server  (start the redis)
  ```

- Status 

  ```sh
  sudo systemctl status redis-server  (redis status)
  ```

- stop and testing 

  ```sh
  sudo service redis-server stop (redis stop)
  redis-cli  (testing)
  ```

### Data Types 

- Key : the name of property
- Strings 
- list
- Hashes (with object-key, field-value pair)
- Set a list of unordered and unique sequence
- Sorted-sets (a user defined unique strings)

### Redis Persistence

-  Append only file (for speed)
  - it uses a log to rebuilt the data
- Redis database file  (for data recovery)
  - take snapshots, creating the copies point in data
- RDB is default 

### Commands for db 

- set the dict (strings)

```sh
set key value  (to set the value)
get key  (to get the value)
incr value (to increase the value by 1)
decr value (to decrease the value by 1)
set country name "South Africa" (set the value of the string)
getset key value (set and get the value asap)
mset key value key value key value  (to set multiple value )
mget key key key key (to get the values)
exists key (to check if that is present) (return 0 or 1 )
set key value exp 10 (given a time when it expires)

```

- set the hashes

  ```sh
  hmset user:567 key value key value key value (set the hash value)
  hmgetall user:567  (get the value of the data)
  hmget user:567 key key key (get the value of user)
  hexists user:567 key (to get the values if exists)
  hincrby user:567 key 78 (to increase byu the value)
  
  ```

- Lists 

  - Fast, need to add at end or beginning, sequential data 

  ```sh
  rpush lst_name value value  (to make a lst and store values)
  lrange lst_name 0 -1  (start last indexing) (to list the value)
  lrange lst_name 0 -2  (to list the value except the last one)
  lpop lst_name (to remove the item)
  rpop lst_name (to remove the item)
  ltrim lst_name start stop  (0 4) (to trim the lst)
  ```

- Sets in redis

  - has the unique collection of the data 

    ```sh
    sadd set_name member member member (the values in the sets)
    smembers (to get the value of the stored items in set)
    sismember set_name member_name
    sadd set_name:sub_category member member member (to add item in subcategory)
    scard set_name (to number of the elements)
    ```
  
- Sorted sets

  - They have user or developer define order

  - They use score that sort the data in specific manner 

    ```sh
    zadd key items items items   (to add the items)
    zrange key 0 -1 withscores   (to get the value with sorted manner)
    zrevrange key 0 -1 withscores   (to get reverse scores)
    zrangebyscore key -inf point withscore (point the value in the db)  (withscore the sorting type)
    ```

### Redis Pubs and Subs 

- it's a publishing and reading system 
- where one publish and other read it 

### Redis with Python

- Installation 

  ```sh
  pip install redis
  ```

- Import 

  ```python
  import redis
  ```

- Connect 

  ```python
  r = redis.Redis(host='localhost', port=6379, db=0)  #defalt port
  ```

### Notes - 

- Redis is a multipurpose tool that has the use cases

- Redis is a no SQL database

- uses a default port 6379

- Redis is implemented with many languages and uses multiple client services

- Redis.conf file has the password and configuration settings

- Redis can be binded by multiple interface but that is not recommended

- Redis cluster and sentient 

- Common redis use case 

  - Cache 
  - Background job queue
  - User session 
  - API throttling
  - Feature Flags

- Pros 

  - data store and job queue
  - Flexible data structure
  - Speed

- Cons

  - RAM usage 
  - Cannot query by the value


### Links 

```text
https://linuxize.com/post/how-to-install-and-configure-redis-on-ubuntu-18-04/
https://redis.io/topics/quickstart
https://www.youtube.com/watch?v=Koh6piVaYh0
https://github.com/redis/redis-py
https://www.youtube.com/watch?v=dlI-xpQxcuE
https://redis-py.readthedocs.io/en/stable/  (documenatation)
https://realpython.com/python-redis/  (documenatation)
```

