from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.models import Task
from backend.serializers import TaskSerializer


@api_view(['GET', 'POST'])
def tasks(request):
    if request.method == "GET":
        all_tasks = Task.objects.all()
        serializer = TaskSerializer(all_tasks, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            _task = serializer.save()
            response_data = {
                'message': 'Food item created successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['PUT', 'DELETE'])
def update_task(request, id):
    if request.method == "PUT":
        task = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(task, data=request.data, partial=True)  # Use partial=True for partial updates
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Task updated successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=200)
        return Response(serializer.errors, status=400)
    elif request.method == "DELETE":
        task = get_object_or_404(Task, id=id)
        task.delete()
        return Response({'message': 'Task deleted successfully!'}, status=204)
