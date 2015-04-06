# spam/__init__.py

from .foo import *
from .bar import *

__all__ = (foo.__all__ + bar.__all__)
