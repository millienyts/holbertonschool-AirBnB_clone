# Inside models/__init__.py
from models.engine import FileStorage

storage = FileStorage()
storage.reload()
