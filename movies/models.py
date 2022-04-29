from django.db import models

# Create your models here.

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=70)
    released_year = models.CharField(max_length=20)
    rating = models.CharField(max_length=20)
    generes = models.JSONField()

    class Meta:
        managed = True
        db_table = 'movies'