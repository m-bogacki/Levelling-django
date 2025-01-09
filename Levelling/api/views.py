from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

# Create your views here.


class UserListCreateView(ListCreateAPIView):

    serializer_class = None

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
