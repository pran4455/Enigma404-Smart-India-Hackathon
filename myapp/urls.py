from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload_audio/', views.upload_audio, name='upload_audio'),
    path('play_audio/<int:audio_id>/', views.play_audio, name='play_audio'),
    path('get_latest_audio_id/', views.get_latest_audio_id, name='get_latest_audio_id'),
    path('record_audio/', views.record_audio, name='record_audio'),
    path('play_latest_audio/', views.play_latest_audio, name='play_latest_audio'),
    path('play_latest_audio_page/', views.play_latest_audio_page, name='play_latest_audio_page'),
    path('enigma404/get_latest_audio_page/', views.play_latest_audio_page, name='play_latest_audio_page'),
    path('enigma404/get_latest_audio/', views.play_latest_audio, name='play_latest_audio'),
    path('enigma404/get_audio_data/', views.get_audio_data, name='get_audio_data'),
    path('get_audio_data/', views.get_audio_data, name='get_audio_data'),
]