# watcher.py
#
# Import hook that simply prints out what's being imported

import sys

class Watcher(object):
    @classmethod
    def find_spec(cls, name, path, target=None):
        print('Importing', name, path, target)
        return None

sys.meta_path.insert(0, Watcher)

