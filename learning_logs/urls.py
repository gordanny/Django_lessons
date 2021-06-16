"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # List of topics.
    path('topics/', views.topics, name='topics'),
    # List of entries for topics.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for add new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for add new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for edit the entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
