# webhook.py

import re
import urllib.request
import sys
import importlib.util

def url_hook(name):
    if not name.startswith(('http:', 'https:')):
        raise ImportError()
    data = urllib.request.urlopen(name).read().decode('utf-8')
    filenames = re.findall('[a-zA-Z_][a-zA-Z0-9_]*\.py', data)
    modnames = { name[:-3] for name in filenames }
    return UrlFinder(name, modnames)

class UrlFinder(object):
    def __init__(self, baseuri, modnames):
        self.baseuri = baseuri
        self.modnames = modnames

    def find_spec(self, modname, target=None):
        if modname in self.modnames:
            origin = self.baseuri + '/' + modname + '.py'
            loader = UrlLoader()
            return importlib.util.spec_from_loader(modname,
                                      loader, origin=origin)
        else:
            return None

class UrlLoader(object):
    def create_module(self, target):
        return None

    def exec_module(self, module):
        u = urllib.request.urlopen(module.__spec__.origin)
        code = u.read()
        compile(code, module.__spec__.origin, 'exec')
        exec(code, module.__dict__)

sys.path_hooks.append(url_hook)
