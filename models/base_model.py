#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models  # Ensure this import is at the top to avoid circular imports

class BaseModel:
    """Defines all common attributes/methods for other classes."""
    
    def __init__(self, *args, **kwargs):
        """Initialization of the base model."""
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    # Correct datetime conversion for deserialization
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            self.id = kwargs.get("id", str(uuid4()))
            self.created_at = kwargs.get("created_at", datetime.now())
            self.updated_at = kwargs.get("updated_at", datetime.now())
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)  # Link the instance with FileStorage upon creation

    def __str__(self):
        """String representation of the BaseModel class."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute `updated_at` with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance."""
        dictionary = dict(self.__dict__)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
