from django.urls import path
from . import views

urlpatterns = [
    path('led/<int:luminance>', views.led, name='led'),
    path('video/<int:binary_picture>', views.video, name='video')
]