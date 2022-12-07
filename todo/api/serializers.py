from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('task',)

class IDTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id',)