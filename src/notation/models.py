from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class NotesCategories(models.Model):
    title = models.CharField(max_length=10, default='categoriesTitle')


class NotationTable(models.Model):
    date = models.DateField("Date", default=datetime.today)
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *agrs, **kwargs):
        super(NotationTable, self).save(*agrs,**kwargs)
        return self

class Note(models.Model):
    id = models.IntegerField(primary_key=True)
    table = models.ForeignKey(NotationTable, on_delete=models.CASCADE)
    valeur = models.IntegerField()
    categories = models.ForeignKey(NotesCategories, on_delete=models.PROTECT)

