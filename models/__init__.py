#!/usr/bin/env python3
""" The module creates a storage variable imported from filestorage.py"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
