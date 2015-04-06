# spam.py

from importlib.util import find_spec

if find_spec('foo'):
    import foo
else:
    import simplefoo as foo

