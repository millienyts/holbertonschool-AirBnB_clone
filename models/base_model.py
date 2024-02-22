from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance."""
        model_dict = dict(self.__dict__)
        model_dict["__class__"] = self.__class__.__name__
        model_dict["created_at"] = model_dict["created_at"].isoformat()
        model_dict["updated_at"] = model_dict["updated_at"].isoformat()
        return model_dict
