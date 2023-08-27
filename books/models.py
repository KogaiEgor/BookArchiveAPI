from django.db import models

class Book(models.Model):
    name = models.CharField()
    author = models.CharField()
    publishing_date = models.DateField()

