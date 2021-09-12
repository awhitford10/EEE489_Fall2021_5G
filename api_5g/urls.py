from django.urls import path
from . import views

urlpatterns = [
    path('/led/<int:luminance>', views.led, name='led'),
    path('/video', views.video, name='video')
]