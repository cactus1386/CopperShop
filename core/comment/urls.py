from django.urls import path, include
from .views import CommentView

urlpatterns = [
    path('comment/', CommentView.as_view(), name='comment-api')
]
