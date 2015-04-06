# tool.py

print("I'm a tool.")

import sys
import os.path

def main():
    if len(sys.argv) < 2:
        raise SystemExit('Usage: python3 -m tool script.py')
    sys.argv[:] = sys.argv[1:]
    progname = sys.argv[0]
    sys.path.insert(0, os.path.dirname(progname))
    with open(progname, 'rb') as fp:
         code = compile(fp.read(), progname, 'exec')
    globs = {
         '__file__' : progname,
         '__name__' : '__main__',
         '__package__' : None,
         '__cached__' : None
    }
    exec(code, globs)

if __name__ == '__main__':
    main()
