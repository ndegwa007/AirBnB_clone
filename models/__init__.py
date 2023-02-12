<<<<<<< HEAD
#!/usr/bin/env python3
""" The module creates a storage variable imported from filestorage.py"""
=======
#!/usr/bin/python3 
""" __init__ magic method for models directory """
>>>>>>> 9cdb8b390178a6a64d580661fdcc1682a6ef035a

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
