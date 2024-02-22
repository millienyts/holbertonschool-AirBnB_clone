#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Defines all common attributes/methods for other classes."""
    
    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

  def save(self):
        """Updates updated_at with the current datetime and saves to file."""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def __init__(self, *args, **kwargs):
        """Initialization of the base model."""
        # existing initialization logic...
        if not kwargs:
            storage.new(self)
            
    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        model_dict = dict(self.__dict__)
        model_dict["__class__"] = self.__class__.__name__
        model_dict["created_at"] = model_dict["created_at"].isoformat()
        model_dict["updated_at"] = model_dict["updated_at"].isoformat()
        return model_dict
