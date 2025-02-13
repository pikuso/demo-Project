from django.urls import path
from .views import home, about, programs, contact

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('programs/', programs, name='programs'),
    path('contact/', contact, name='contact'),
]
