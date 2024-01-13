from django.urls import path
from .views import index



#All main urls endpoints will be recieved here first then routed where they should be. This is the main hub per say. 
urlpatterns = [
    path('', index),
]