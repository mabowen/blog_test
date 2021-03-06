from django.urls import path
from . import views
from . import forms

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/',views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/del/', views.post_del, name='post_del'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
]
