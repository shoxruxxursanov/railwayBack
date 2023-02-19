from django.urls import path
from .views import UserCreationView, SignInView

urlpatterns = [
    path('signup/', UserCreationView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
]