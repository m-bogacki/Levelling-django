from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import TaskSerializer
from .models import Task

# Create your views here.


class TaskView(ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):

        # If user is admin, return all tasks
        if self.request.user.role == 3:
            return Task.objects.all()

        # If user is not admin, return only their tasks
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        return super().perform_create(serializer)
