# spam/__init__.py

# List the exported symbols by module
_submodule_exports = {
    '.foo' : ['Foo'],
    '.bar' : ['Bar']
}

# Make a {name: modname } mapping
_submodule_by_name = {
     name: modulename 
           for modulename in _submodule_exports
           for name in _submodule_exports[modulename] }

import types, sys, importlib

class OnDemandModule(types.ModuleType):
    def __getattr__(self, name):
        modulename = _submodule_by_name.get(name)
        if modulename:
            module = importlib.import_module(modulename, 
                                             __package__)
            print('Loaded', name)
            value = getattr(module, name)
            setattr(self, name, value)
            return value
        raise AttributeError('No attribute %s' % name)

newmodule = OnDemandModule(__name__)
newmodule.__dict__.update(globals())
newmodule.__all__ = list(_submodule_by_name)
sys.modules[__name__] = newmodule
