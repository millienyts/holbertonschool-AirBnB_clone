#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """Base class for all models."""
    
    def __init__(self, *args, **kwargs):
        """Initialization of the base model."""
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
    
    def __str__(self):
        """String representation of the BaseModel class."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """Updates `updated_at` with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        """Converts instance into a dictionary format."""
        model_dict = dict(self.__dict__)
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
