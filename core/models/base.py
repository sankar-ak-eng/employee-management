from django.db import models
from django.utils import timezone

class BaseModelMeta(models.base.ModelBase):
    """
    Reorders inherited BaseModel fields to be at the end
    """
    def __new__(cls, name, bases, attrs):
        # If 'BaseModel' is in bases, reorder its fields
        new_class = super().__new__(cls, name, bases, attrs)
        if hasattr(new_class, '_meta'):
            fields = list(new_class._meta.fields)
            # Move created_at and updated_at to the end
            reordered = [f for f in fields if f.name not in ('created_at', 'updated_at')]
            for f in fields:
                if f.name in ('created_at', 'updated_at'):
                    reordered.append(f)
            new_class._meta.fields = reordered
        return new_class
    
    
class BaseModel(models.Model, metaclass=BaseModelMeta):
    # set once when object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # updated every time object is saved
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # This model will not create a table in the DB
        abstract = True