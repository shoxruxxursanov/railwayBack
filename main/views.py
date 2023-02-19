from rest_framework import generics
from .models import Person
from .serializer import PersonSerializer

from drf_yasg.utils import swagger_auto_schema

class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer