from tkinter.font import names

from django.urls import path
from .views import PostListView

urlpatterns = [
    path('posts/', PostListView.as_view())
]

