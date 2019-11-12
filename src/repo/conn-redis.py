import redis

host = "localhost"
r = redis.Redis(host=host, port=6379, db=0)
data = r.hget("name", "key")

print(data.decode("utf-8"))
