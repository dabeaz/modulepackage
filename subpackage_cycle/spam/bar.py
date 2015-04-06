# bar.py

try:
    from . import foo
except ImportError:
    import sys
    foo = sys.modules[__package__ + '.foo']

print('imported spam.bar')
