from distutils.core import setup

try:
    with open('README.rst') as file:
        long_description = file.read()
except:
    long_description = 'Dathost-python\n==============\n\nThis is a python wrapper for the dathost API.\n\nInstallation\n------------\n\n.. code:: python\n\n    pip3 install dathostpython\n\nBasic usage\n-----------\n\n.. code:: python\n\n    from dathostpython.wrapper import dathost\n\n    dathost = dathost("email", "password")\n\n    # List servers and all their details\n    print(dathost.servers())\n\n    # Start a server\n    dathost.start("server id")\n\n    # Stop a server\n    dathost.stop("server id")\n\n    # Duplicate a server\n    dathost.duplicate("server id")\n\n    # Duplicate a server and print its id\n    print(dathost.duplicate("server id")["id"])\n\n    # Delete a server\n    dathost.delete("server id")\n\n    # Retrieve a file from the server\n    dathost.getFile("server id", "path/to/file.txt")\n\n    # Retrieve info on a server\n    print(dathost.info("server id"))\n\n    # Edit a server value\n    # Multiple values can be passed, for example:\n    # dathost.edit("570e1dadcde5f5xxxxxxxxxx", csgo_settings__rcon = "Bob", name = "Bob")\n    # \n    # Note:\n    # For parameters with "." in them, replace the "." with "__".\n    # A full list of parameters can be found at https://dathost.net/api#!/default/put_game_server_item\n    dathost.edit("server id", parameter = "value" )\n\n    # List files in a directory\n    # The final 2 parameters (Hide default files and show file sizes) are optional\n    dathost.files("server id", "path/to/dir/", True, True)\n\n    # Sync the files between the local cache and the gameserver\n    dathost.sync("server id")'
setup(
  name = 'dathostpython',
  packages = ['dathostpython'],
  version = '1.3.3',
  description = 'A python wrapper for the Dathost API',
  long_description = long_description,
  author = 'Miles Budden',
  author_email = 'miles@budden.net',
  url = 'https://github.com/pbexe/dathost-python',
  keywords = ['dathost', 'hosting', 'wrapper'],
  classifiers = [],
  install_requires=['requests'],
)
