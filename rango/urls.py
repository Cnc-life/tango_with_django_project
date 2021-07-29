from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from rango import views, admin

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
