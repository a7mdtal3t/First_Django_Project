from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ahmed', views.ahmed, name='ahmed'),
    path('hi', views.hi, name='hi'),
    path('zeina', views.zeina, name='zeina')

]
