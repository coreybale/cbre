from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# about Model


class About(models.Model):
    title = models.CharField(blank=True, null=True, max_length=150)
    description = RichTextField(blank=True, null=True, max_length=3000)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
