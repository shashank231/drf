from asyncore import read
from cgitb import lookup
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from . models import *


# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = "__all__"

# class BookSerializer(serializers.ModelSerializer):
#     writer = AuthorSerializer()
#     class Meta:
#         model = Book
#         fields = "__all__"


# class AuthorSerializer(serializers.ModelSerializer):
#     bok = BookSerializer(read_only=True, many=True)
#     class Meta:
#         model = Author
#         fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class AuthorCreateSerializer(serializers.ModelSerializer):
    #bok = BookSerializer(read_only=True, many=True)
    class Meta:
        model = Author
        fields = ['name', 'city', 'capital', 'scity']

class AuthorListSerializer(serializers.ModelSerializer):
    #bok = BookSerializer(read_only=True, many=True)
    class Meta:
        model = Author
        fields = ['name', 'city', 'capital', 'scity']

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"

class MallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mall
        fields = "__all__"

class ParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = "__all__"
        #lookup_field = 'loc'





