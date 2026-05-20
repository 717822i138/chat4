from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),  # உங்க சாட்பாட் வியூவோட பேரு 'chat'-னு இருந்தா இது கரெக்ட் தம்பி!
]
