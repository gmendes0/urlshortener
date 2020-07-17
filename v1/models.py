from django.db import models


class Link(models.Model):
    original = models.CharField(max_length=255)
    hashed = models.CharField(max_length=50)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'links'

    def __str__(self):
        return self.hashed
