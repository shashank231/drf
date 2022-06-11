from django.urls import path

from apip2 import views

urlpatterns = [
    path('Department/', views.DepartmentView.as_view()),
    path('Department/<int:pk>', views.DepartmentDetailsView.as_view()),

    path('Teacher/', views.TeacherView.as_view()),
    path('Teacher/<int:pk>', views.TeacherDetailsView.as_view()),

    path('Clas/', views.ClasView.as_view()),
    path('Clas/<int:pk>', views.ClasDetailsView.as_view()),

    path('Floor/', views.FloorView.as_view()),
    path('Floor/<int:pk>', views.FloorDetailsView.as_view())

]