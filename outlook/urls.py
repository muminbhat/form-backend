from django.urls import path
from .views import post_create_leave
urlpatterns = [
    path('post/', post_create_leave, name='newsletter-create'),  
]
