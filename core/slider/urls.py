from django.urls import path
from . import views

urlpatterns = [
    path('slider/', views.SliderViews.as_view(), name='slider-list'),
]
