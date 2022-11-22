from rest_framework import serializers

from tracker.models import IssueTracker, Project


class StatusSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class TypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'start_date', 'end_date', 'description']
        read_only_fields = ['id', 'start_date', 'end_date']


class TaskSerializer(serializers.ModelSerializer):
    status = StatusSerializer(read_only=True)
    type = TypeSerializer(read_only=True, many=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = IssueTracker
        fields = ['summary', 'description', 'status', 'project', 'type', 'created_at', 'changed_at', 'is_deleted']
        read_only_fields = ['id', 'status', 'type', 'project', 'created_at', 'changed_at', 'is_deleted']
