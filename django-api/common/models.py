from django.core.checks.messages import Error
from django.db import models


# This is a BaseModel to be used by other models (Post Model)
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Prevents Django creating BaseModel table (migration)
    # https://docs.djangoproject.com/en/4.0/topics/db/models/#abstract-base-classes-1
    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    all_objects = models.Manager()

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    def delete(self):
        raise Error()

    class Meta:
        abstract = True
