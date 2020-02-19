from __future__ import unicode_literals
from django.db import models
from datetime import datetime, date



class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {

        }

        if len(postData['title']) < 2:
            errors['title'] = "Title should be at least 2 characters long!"
        if Show.objects.filter(title=postData['title']).exists():
            errors['title_repeat'] = "Title should be unique!"
        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters long!"
        if len(postData['desc']) < 10 and len(postData['desc']) is not 0:
            errors['desc'] = "Description should be at least 10 characters long!"
        return errors



class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Show info title: {self.title} | netword: {self.network}"

    