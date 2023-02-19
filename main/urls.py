from django.urls import path,include
from .views import PersonListCreateView, PersonRetrieveUpdateDestroyView
from django.contrib.auth.views import LoginView

urlpatterns = [
    # path('api/',include('api.urls')),
    # path('register/', UserRegistration.as_view(), name='register'),
    path('persons/', PersonListCreateView.as_view(), name='person-list-create'),
    path('persons/<int:pk>/', PersonRetrieveUpdateDestroyView.as_view(), name='person-retrieve-update-destroy'),

]