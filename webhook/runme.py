# runme.py
#
# Before running this, go to the 'files' directory and 
# execute 'python3 -m http.server' in a different process

import webhook
import sys
sys.path.append('http://localhost:8000')

import foo
import bar
print(foo)
print(bar)
