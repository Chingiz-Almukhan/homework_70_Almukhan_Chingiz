from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializer import TaskSerializer
from tracker.models import IssueTracker


class TaskView(APIView):
    def get(self, request, *args, **kwargs):
        objects = get_object_or_404(IssueTracker, pk=kwargs['pk'])
        serializer = TaskSerializer(objects)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        objects = get_object_or_404(IssueTracker, pk=kwargs['pk'])
        serializer = TaskSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data='Wrong parameters')


class DeleteTaskView(APIView):
    def delete(self, request, *args, **kwargs):
        objects = get_object_or_404(IssueTracker, pk=kwargs['pk'])
        objects.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
