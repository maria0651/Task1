from django.urls import path
from firstapplication import views

urlpatterns = [
    path('first', views.index,name="index"),
    path('', views.template_demo, name="index),")

]