from cgitb import lookup
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from . models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    dep = serializers.CharField(source = 'dep.name', read_only=True)
    dlvl = serializers.CharField(source = 'dep.lvl', read_only=True)
    class Meta:
        model = Teacher
        fields = "__all__"
        #['name', 'pay', 'dep']            # aise b kar sakte but no need, beacuse, "__all__" apne aap ['dep', 'dlvl'] or ['name', 'pay'] ko b lelega                             

class ClasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clas
        fields = "__all__"


class FloorSerializer(serializers.ModelSerializer):
    #cls = serializers.IntegerField(source='cls.grade')                                         # ye cls ko ocerride kar dega payload me, but shouldn't do this because ye FKEY hai
    floor_master = serializers.CharField(source='cls.master.name', read_only=True)              # jin fields me aise '.' a jati hai they can't be accessed while creating, gives error
    floor_master_dep = serializers.CharField(source='cls.master.dep.name', read_only=True)
    class Meta:
        model = Floor
        fields = "__all__"
  