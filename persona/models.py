from django.db import models

# Create your models here.

class Persona(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=40)
    color = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'auto'

    def __str__(self):
        return self.marca

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_start = models.IntegerField()

    def __str__(self):
        return self.name





