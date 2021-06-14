from django.urls import path
from . import views
from .config import BOT_TOKEN

app_name = 'updates'
urlpatterns = [
    path('', views.index, name="index"),
    path('sendEMessage', views.send_message_to_everyone, name="send_message_to_everyone"),
    path(BOT_TOKEN, views.get_updates),
]