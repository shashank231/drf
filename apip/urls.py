
from django.urls import path

from apip import views

urlpatterns = [
    path('Shop/', views.ShopView.as_view()),
    path('Shop/<int:pk>', views.ShopDetailsView.as_view()),


    path('Mall/', views.MallView.as_view()),
    path('Mall/<int:pk>', views.MallDetailsView.as_view()),


    path('Book/', views.BookView.as_view()),
    path('Book/<int:pk>', views.BookDetailsView.as_view()),


    path('Author/', views.AuthorView.as_view()),
    path('Author/<int:pk>', views.AuthorDetailsView.as_view()),


    path('Park/', views.ParkView.as_view()),
    path('Park/<int:pk>', views.ParkDetailsView.as_view()),
    path('Par/<int:pin>', views.ParkPin.as_view()),


    path('Org/', views.OrgView.as_view()),
    path('Org/<int:id>', views.OrgDetailsView.as_view())
]

