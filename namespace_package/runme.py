# Illustrate how two packages become one if there's no __init__

import sys
sys.path.extend(['spam_foo', 'spam_bar'])

import spam.foo
import spam.bar

print(spam.foo.__file__)
print(spam.bar.__file__)
