# redisloader.py                                                                                                                                   
import redis
import importlib.util

class RedisImporter(object):
    def __init__(self, *args, **kwargs):
        self.conn = redis.Redis(*args, **kwargs)
        self.conn.exists('test')

    def find_spec(self, name, path, target=None):
        origin = name + '.py'
        if self.conn.exists(origin):
            loader = RedisLoader(origin, self.conn)
            return importlib.util.spec_from_loader(name, loader)
        return None

def enable(*args, **kwargs):
    import sys
    sys.meta_path.insert(0, RedisImporter(*args, **kwargs))

class RedisLoader(object):
    def __init__(self, origin, conn):
        self.origin = origin
        self.conn = conn

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        code = self.conn.get(self.origin)
        exec(code, module.__dict__)
