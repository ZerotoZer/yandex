import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class ShopUnit(models.Model):
    offer = 'OFFER'
    category = 'CATEGORY'
    type_choices = [
        (offer, 'OFFER'),
        (category, 'CATEGORY'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    parentId = models.UUIDField(default=uuid.uuid4, editable=False, null=True)
    type = models.CharField(
        max_length=10,
        choices=type_choices,
        editable=False,
    )
    price = models.IntegerField(null=True)
