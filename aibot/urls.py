from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatbot.urls')), # இது கரெக்டா chatbot.urls-ஐ மட்டும் தான் கூப்பிடணும்
]