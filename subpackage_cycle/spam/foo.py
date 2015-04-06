# foo.py

try:
    from . import bar
except ImportError:
    import sys
    bar = sys.modules[__package__ + '.bar']

print('imported spam.foo')

