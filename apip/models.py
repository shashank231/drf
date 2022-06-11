from turtle import mode
from unicodedata import lookup
from django.db import models
from django.core.exceptions import ValidationError

def validate_city(value):
    print("--------------------------------------------------------------------------------------------")
    print(value)
    if len(value) == 3:
        print("{{{{{{{{{{{{")
        raise ValidationError("city can not be empty")

class Author(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50, validators=[validate_city])

    def scity(self):
        return str(self.city + ' CITY')

    @property
    def capital(self):
        return 'CAPITAL ME NAME'


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    writer = models.ForeignKey(Author, related_name='bok', on_delete=models.CASCADE)

    def clean(self):
        super().clean()
        if self.rating == 2:
            raise ValidationError({'error':'2 is not aloud'})

    def save(self, *args, **kwargs):
        self.clean()
        super(Book, self).save(*args, **kwargs)                                                                                                                                         



class Shop(models.Model):
    name = models.CharField(max_length=50)
    addr = models.CharField(max_length=50)

class Mall(models.Model):
    name = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
        

class Park(models.Model):
    name = models.CharField(max_length=50)
    loc = models.IntegerField(primary_key=True)
    lookup_field = 'loc'

