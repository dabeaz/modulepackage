# Test the redisloader

import redisloader
import redis

redisloader.enable()

r = redis.Redis()
r.set('foo.py', 'print("imported foo")')

import foo
print(foo)
