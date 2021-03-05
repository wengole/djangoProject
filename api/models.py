from uuid import uuid4

from django.db import models


class Consumer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.TextField()
    last_name = models.TextField()
    income = models.IntegerField(default=0)
