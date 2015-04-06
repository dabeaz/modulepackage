import os
import os.path

# For user-home directory use this
# user_plugins = os.path.expanduser('~/.telly')

# For tutorial just use current directory
user_plugins = 'telly-contrib'

if os.path.exists(user_plugins):
    plugins = os.listdir(user_plugins)
    for plugin in plugins:
        __path__.append(os.path.join(user_plugins, plugin))
