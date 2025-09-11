from django.urls import path
from .views import RegisterView,LoginProfileView

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('profile/',LoginProfileView.as_view(),name='profile'),
]