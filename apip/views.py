# monti 123

from gc import get_objects
import imp
from django.http import Http404
from django.shortcuts import render
from . models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError

from django.shortcuts import get_object_or_404

class ShopView(APIView):

    def get(self, request, *args, **kwargs):
        dat = Shop.objects.all()
        ser = ShopSerializer(instance=dat, many=True)
        return Response(ser.data)

    def post(self, request, *args, **kwargs):
        dat = request.data
        ser = ShopSerializer(data = dat)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

class ShopDetailsView(APIView):

    def get_object(self,pk):
        try:
            return Shop.objects.get(pk=pk)
        except Shop.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        shp = self.get_object(pk)
        ser = ShopSerializer(shp)
        return Response(ser.data)

    def put(self,request,pk):
        shp = self.get_object(pk)
        ser=ShopSerializer(instance= shp, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BA)

    def delete(self,request,pk):
        shp = self.get_object(pk)
        shp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class MallView(generics.GenericAPIView):
    queryset = Mall.objects.all()
    serializer_class = MallSerializer

    def get(self, request, *args, **kwargs):
        dat = super().get_queryset()
        ser = super().get_serializer(instance = dat, many=True)
        return Response(ser.data)

    def post(self, request, *args, **kwargs):
        dat = request.data
        ser = super().get_serializer(data=dat)
        ser.is_valid(raise_exception = True)
        ser.save()
        return Response(ser.data)

class MallDetailsView(generics.GenericAPIView):
    serializer_class = MallSerializer

    def get_object(self,pk):
        try:
            return Mall.objects.get(pk=pk)
        except Mall.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        mal = self.get_object(pk)
        ser = super().get_serializer(instance=mal)
        return Response(ser.data)

    def put(self,request,pk):
        mal = self.get_object(pk)
        ser = super().get_serializer(instance= mal, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BA)

    def delete(self,request,pk):
        mal = self.get_object(pk)
        mal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class StudentList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class= StudentSerializer

#     def get(self,request):
#         return self.list(request)

#     def post(self,request):
#         return self.create(request)

# class StudentDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class= StudentSerializer

#     def get(self,request,pk):
#         return self.retrieve(request,pk)

#     def put(self,request,pk):
#         return self.update(request,pk)

#     def delete(self,request,pk):
#         return self.destroy(request,pk)




class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def post(self, request, *args, **kwargs):
    #     print(request.data)
    #     request.data.update({'rating': 9})
    #     request.data.update({'writer': 2})
    #     print(request.data)
    #     return super(BookView, self).post(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        try:
            return super(BookView, self).post(request, *args, **kwargs)
        except ValidationError as e:
            return Response(e.error_dict)

class BookDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer




class AuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AuthorCreateSerializer
        return AuthorListSerializer

class AuthorDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer




class ParkView(generics.ListCreateAPIView):
    queryset = Park.objects.all()
    serializer_class = ParkSerializer

class ParkDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Park.objects.all()
    serializer_class = ParkSerializer
    #lookup_field = 'loc'

class ParkPin(generics.ListAPIView):
    serializer_class = ParkSerializer

    def get_queryset(self):
        p1 = self.kwargs['pin']
        return Park.objects.filter(loc__gt = p1)





class OrgView(generics.ListCreateAPIView):
    queryset = Org.objects.all()
    serializer_class = OrgListSerializer

class OrgDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Org.objects.all()
    lookup_field = "id"

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return OrgPostSerializer
        return OrgListSerializer

    def put(self, request, *args, **kwargs):
        try:
            super(OrgDetailsView, self).put(request, *args, **kwargs)
        except ValidationError as e:
            # print("e.erroe_dict = ", e.error_dict)
            # return Response(e.eroor_dict)        --------->      if raise Validationerror from models.py
            return Response(e)                   # --------->      if raise Validationerror from serializers.py

    # def get_object(self):
    #     rank = self.kwargs.get("rank")
    #     name = self.kwargs.get("name")
    #     return get_object_or_404(Org, name=name, rank=rank)

    # path('Org/<int:orgid>', views.OrgDetailsView.as_view())
    # lookup_field = 'orgid'                                     # Cannot resolve keyword 'orgid' into field. Choices are: id, name, org_id, rank

    #path('Org/<int:org_id>', views.OrgDetailsView.as_view())
    #lookup_field = 'org_id'                                     # org_id se dhundega, works properly

    # url me pk set karo to lookup_field= "pk" hi rakhna parega, na b rakho to kaam karta
    # url me id set karo to lookup_field= "id" hi rakhna parega, nahi rakha to kaam nahi karta




