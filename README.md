#Dathost-python

This is a python wrapper for the dathost API.

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
```