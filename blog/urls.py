from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
path('drafts/', views.post_draft_list, name='post_draft_list'),

path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),

path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),

path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),