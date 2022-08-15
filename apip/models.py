from lib2to3.pytree import Base
from turtle import mode
from unicodedata import lookup
from django.db import models
from django.core.exceptions import ValidationError
import re


def validate_city(value):
    print("--------------------------------------------------------------------------------------------")
    print(value)
    if len(value) == 3:
        print("{{{{{{{{{{{{")
        raise ValidationError("city can not be empty")

class Base(models.Model):
    created = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated = models.DateTimeField(auto_created=True, auto_now=True)
    is_deleted = models.BooleanField(default=False)

    @staticmethod
    def normalize(input_str):
        input_str = re.sub(r'[^a-zA-Z0-9]', '', input_str)
        return input_str.upper()

class Author(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50, validators=[validate_city])

    def scity(self):
        return str(self.city + ' CITY')

    @property
    def capital(self):
        return 'CAPITAL ME NAME'

class Book(Base):
    title = models.CharField(max_length=50)
    normalize_title = models.CharField(max_length=50, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    writer = models.ForeignKey(Author, related_name='bok', on_delete=models.CASCADE)

    # def clean(self):
    #     super().clean()
    #     if self.rating == 2:
    #         raise ValidationError({'error':'2 is not aloud'})

    # def save(self, *args, **kwargs):
    #     self.clean()
    #     super(Book, self).save(*args, **kwargs)                                                                                                                                         

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.normalize_title = Book.normalize(self.title)
        super(Book, self).save(force_insert, force_update, using, update_fields)

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

class Org(models.Model):
    org_id = models.CharField(max_length=50, null=False, unique=True)
    name = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
