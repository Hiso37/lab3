import time
import redis

r = redis.Redis(host="db", port=6379, decode_responses=True)  # db = ім'я сервісу
while True:
    count = r.incr("visits")
    print(f"LAB WORK NUMBER 3. = {count}", flush=True)
    time.sleep(3)