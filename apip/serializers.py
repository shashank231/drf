from rest_framework import serializers
from . models import *
import re

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

def validate_book_title(name):
    print("aya aya aya aya aya aya ")
    print("1")
    print("222222222222222")
    name_reg_ex = r"^[a-z0-9][a-z0-9_]*$"
    error_msg = None

    if not name or len(name) < 1 :
        error_msg = 'Book name is required.'
    if not re.search(name_reg_ex, name):
        error_msg = "Space and special characters except underscore('_') are not allowed. "
        error_msg += "Book name should not have uppercase letters."

    if error_msg:
        raise ValidationError({"validation_error": True, "name": [error_msg]})

class BookSerializer(serializers.ModelSerializer):
    writer_name = serializers.CharField(source='writer.name', read_only = True)
    normalize_title = serializers.CharField(read_only=True)    

    def validate(self, attrs):
        title = attrs['title']
        print(title)
        print("----------------------------------")
        validate_book_title(title)
        # not ideal because we are replicating logic
        # exists = Book.objects.filter(normalized_name=Book.normalize(title), org_id=attrs['org']).count() > 0
        # if exists:
        #     raise ValidationError({"name": ["Name is not unique to org."]})
        return attrs

    class Meta:
        model = Book
        fields = "__all__"
        #fields = ["writer_name", "title", "writer", "id", "rating"]

class AuthorCreateSerializer(serializers.ModelSerializer):
    #bok = BookSerializer(read_only=True, many=True)
    class Meta:
        model = Author
        fields = ['name', 'city', 'capital', 'scity']

class AuthorListSerializer(serializers.ModelSerializer):
    bok = BookSerializer(read_only=True, many=True)
    class Meta:
        model = Author
        fields = ['name', 'city', 'capital', 'scity', 'bok']

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

class OrgPostSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        if validated_data['name'] == "abcd":
            raise ValidationError("abcd nahi chalega bhai")
        return super().update(instance, validated_data)

    class Meta:
        model = Org
        fields = ["org_id", "rank"]

class OrgListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Org
        fields = "__all__"


