from django.urls import path
from . import views

#. represent the pwd we are importing the views file htat we have craeted

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),

]