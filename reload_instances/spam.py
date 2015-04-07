# spam.py
#
# A class that detects reloading and flips all existing instances to the
# new class by changing their __class__ attribute.

import weakref
class Spam(object):
    if 'Spam' in globals():
       _instances = Spam._instances
    else:
       _instances = weakref.WeakSet()

    def __init__(self):
        Spam._instances.add(self)

    def yow(self):
        print('Yow!')     # Try changing this and reloading

for instance in Spam._instances:
    instance.__class__ = Spam
