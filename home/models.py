from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


# Create your models here.

class MenuItem(MPTTModel):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title

    # db.sqlite3