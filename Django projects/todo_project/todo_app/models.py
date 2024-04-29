from django.db import models

class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    is_checked = models.BooleanField(default=False)
