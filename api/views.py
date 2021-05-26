from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import TaskSerializer
from api.models import Task


# All urls ToDo app
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/task-list/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls, status=status.HTTP_200_OK)


# Get all Todo
@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Create new Todo
@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


# Update Todo
@api_view(['PATCH'])
def task_update(request, pk):
    task = Task.objects.filter(id=pk).first()
    if not task:
        return Response({"message": "Not found Task"})
    serializer = TaskSerializer(instance=task, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)


# Delete Todo
@api_view(['DELETE'])
def task_delete(request, pk):
    task = Task.objects.filter(id=pk).first()
    if not task:
        return Response({"message": "Not found Task"})
    task.delete()
    return Response({"message": "Task deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
