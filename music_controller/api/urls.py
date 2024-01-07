from django.urls import path

#add this
from .views import main




#All main urls endpoints will be recieved here first then routed where they should be. This is the main hub per say. 
urlpatterns = [
    path('', main)
]
