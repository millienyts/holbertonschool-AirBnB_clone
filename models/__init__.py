# Inside models/__init__.py
from models.engine.filestorage import FileStorage

storage = FileStorage()
storage.reload()
