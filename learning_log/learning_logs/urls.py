"""Define url patterns for learning logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('',views.index,name='index'),
    # Topics page
    path('topics/',views.topics,name='topics'),
    # detail page for a single topic
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    # Page for adding new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    ]