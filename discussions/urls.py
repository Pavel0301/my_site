from django.urls import path
from discussions import views
from discussions.models import Discussion
from discussions.views import DiscussionDetailView

app_name = 'discussions_urls'

urlpatterns = [
    path('discussion/create/', views.discussion_create, name='create_discussion'),
    path('discussion/<int:pk>/detail/', DiscussionDetailView.as_view(), name='discussion-detail'),



]
