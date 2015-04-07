# spam.py
#
# A context manager that detects reloaded functions and updates code
# objects--even those imported using 'from module import name'.

from contextlib import contextmanager
import sys
import types

@contextmanager
def reloadable():
    old_funcs = { name: val
                  for name, val in sys._getframe(2).f_globals.items()
                  if isinstance(val, types.FunctionType) }
    yield
    new_funcs = { name: val
                  for name, val in sys._getframe(2).f_globals.items()
                  if isinstance(val, types.FunctionType) }

    changed = new_funcs.items() - old_funcs.items()
    for name, val in changed:
        if name in old_funcs:
            old_funcs[name].__code__ = val.__code__

with reloadable():
    def yow():
        print('Yow!')


