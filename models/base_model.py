#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Defines all common attributes/methods for other classes"""
    
    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """String representation of the BaseModel class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        model_dict = self.__dict__.copy()
        model_dict["__class__"] = self.__class__.__name__
        model_dict["created_at"] = model_dict["created_at"].isoformat()
        model_dict["updated_at"] = model_dict["updated_at"].isoformat()
        return model_dict
