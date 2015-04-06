# Import hook that autoinstall packages
# To test this, suggest using a virtual env

import sys
import subprocess
import importlib.util

class AutoInstall(object):
    _loaded = set()
    @classmethod
    def find_spec(cls, name, path, target=None):
        if path is None and name not in cls._loaded:
            cls._loaded.add(name)
            print("Installing",name)
            try:
                out = subprocess.check_output([sys.executable, '-m', 'pip', 'install', name])
                return importlib.util.find_spec(name)
            except Exception as e:
                print("Failed")
        return None

sys.meta_path.append(AutoInstall)
