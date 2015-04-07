# Modules and Packages : Live and Let Die

*Tutorial Presentation at PyCon'2015.  April 9, 2015.  Montreal.*

This tutorial assumes the use of Python 3.4 or newer.  Certain examples
in sections 8 and 9 require the use of Python 3.5. 

The official website for this tutorial is http://www.dabeaz.com/modulepackage/index.html

## Part 1 - Basic Knowledge

`basic_package/` : A very simple package consisting of multiple files.

## Part 2 - Packages

`package_assembly/` : An example of assembling a package from submodules
by exporting symbols in `__init__.py` files.

`decorator_assembly/`: Assemble a package from submodules using a special
`@export` decortor.

## Part 3 - __main__

`main_wrapper` : An example of writing a module that wraps around a script 
using the `-m` option.

## Part 4 - sys.path

No code samples for this part.

## Part 5 - Namespace Packages

`namespace_package` : A simple namespace package example.

`telly` : A package that uses namespace packages to allow for user-extensible submodules.

## Part 6 - The Module

`mini_import` : A minimalistic implementation of the `import` statement.

`subpackage_cycle` : A package where submodules import each other in a cycle.

`import_patch` : An example of patching the builtin `__import__()` function.

## Part 7 - The Module Reloaded

`reload_instances` : A class that detects reloading and updates instances.

`reload_func` : A context manager that allows reloadable functions to be declared.

## Part 8 - Import Hooks

`trial_import` : A module that tests for another module with `import`

`check_import` : A module that tests for another module using module specs.

`lazy_import` : A module that only executes when accessed for the first time.

`watcher` : A simple import hook.

`autoinstall` : An import hook that automatically installs missing modules.

`redisimport` : An import hook that loads modules from Redis.

## Part 9 - Path Hooks

`webhook` : An import hook that allows URLs to be placed on `sys.path`.
