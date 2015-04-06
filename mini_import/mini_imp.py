# mini_imp.py
#
# A tiny implementation of "import"

import types
import sys

def import_module(modname):
    # Check the module cache
    if modname in sys.modules:
        return sys.modules[modname]

    sourcepath = modname + '.py'
    with open(sourcepath, 'r') as f:
         sourcecode = f.read()
    mod = types.ModuleType(modname)
    mod.__file__ = sourcepath
    code = compile(sourcecode, sourcepath, 'exec')

    # Insert into the module cache prior to exec
    sys.modules[modname] = mod
    exec(code, mod.__dict__)
    
    # Return from the module cache
    return sys.modules[modname]
