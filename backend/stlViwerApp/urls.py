
from django.urls import path
from .views import file_exract
urlpatterns = [
    path('',file_exract, name='get_post'),
   
]
