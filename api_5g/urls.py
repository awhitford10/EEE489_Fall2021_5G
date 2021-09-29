from django.urls import path
from . import views

urlpatterns = [
    path('led/<int:luminance>', views.led, name='led'),
    path('video/<str:picture_data>', views.video, name='video')
]