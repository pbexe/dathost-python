#Dathost-python

This is a python wrapper for the dathost API.

##Installation

```python
pip3 install dathostpython
```

##Basic usage

```python
from dathostpython.wrapper import dathost

dathost = dathost("email", "password")

# List servers and all their details
print(dathost.servers())

# Start a server
dathost.start("server id")

# Stop a server
dathost.stop("server id")

# Duplicate a server
dathost.duplicate("server id")

# Duplicate a server and print its id
print(dathost.duplicate("server id")["id"])

# Delete a server
dathost.delete("server id")

# Retrieve a file from the server
dathost.getFile("server id", "path/to/file.txt")

# Retrieve info on a server
print(dathost.info("server id"))

# Edit a server value
# Multiple values can be passed, for example:
# dathost.edit("570e1dadcde5f5xxxxxxxxxx", csgo_settings__rcon = "Bob", name = "Bob")
# 
# Note:
# For parameters with "." in them, replace the "." with "__".
# A full list of parameters can be found at https://dathost.net/api#!/default/put_game_server_item
dathost.edit("server id", parameter = "value" )

```