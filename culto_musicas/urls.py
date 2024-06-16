from django.contrib import admin
from django.urls import path, include
from culto_musicas import views

app_name = 'culto_musicas'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.musicas, name='musicas'),
]
