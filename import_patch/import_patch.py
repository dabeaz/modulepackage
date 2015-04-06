import builtins

def my_import(modname, *args, imp=__import__):
    print('importing', modname)
    return imp(modname, *args)

builtins.__import__ = my_import
