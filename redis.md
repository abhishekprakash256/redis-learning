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

### Notes - 

- Redis is a no SQL database
- uses a default port 6379
- Redis is implemented with many languages and uses multiple client services







### Links 

```text
https://linuxize.com/post/how-to-install-and-configure-redis-on-ubuntu-18-04/
https://redis.io/topics/quickstart
```

