#!/usr/bin/python3
"""Module that defines init file"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
