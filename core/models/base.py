from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    # set once when object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # updated every time object is saved
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # This model will not create a table in the DB
        abstract = True
