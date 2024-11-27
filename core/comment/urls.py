from django.urls import path, include
from .views import CommentView

urlpatterns = [
    path('comment/<int:pk>/', CommentView.as_view(), name='comment-api')
]
