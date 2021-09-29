from django.urls import path
from . import views

urlpatterns = [
    path('led/<int:luminance>', views.led, name='led'),
    path('video/<str:picture>', views.video, name='video')
]