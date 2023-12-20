import uuid

from django.db import models


class TimeStampModel(models.Model):
    """Abstract model that provide timestamp fields"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ModelWithUUID(TimeStampModel):
    """Abstract model that provide uuid field"""

    uuid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)

    class Meta:
        abstract = True
