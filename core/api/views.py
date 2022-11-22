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