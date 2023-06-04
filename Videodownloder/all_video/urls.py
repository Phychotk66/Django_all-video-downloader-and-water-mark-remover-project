from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('download/<int:video_id>/', views.download_video, name='download'),
    path('remove-watermark/<int:video_id>/', views.remove_watermark, name='remove_watermark'),
]
