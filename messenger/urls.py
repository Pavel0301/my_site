from django.urls import path
from messenger import views

app_name = 'messenger_urls'




urlpatterns = [
    path('chatgpt/', views.chat_view, name='chatgpt'),




]