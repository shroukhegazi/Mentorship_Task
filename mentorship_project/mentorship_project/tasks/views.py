import logging
from .models import Task
from rest_framework.decorators import api_view
from .serializers import TaskSerializer, UpdateTaskSerializer
from rest_framework import status, filters
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

def is_status_changeable(current_status, target_status):

    if current_status == "Archived":
        return False

    if current_status == "Done" and target_status == "Draft":
        return False

    if current_status == "Active" and target_status == "Draft":
        return False

    elif current_status == "Draft" and target_status == "Done":
        return False 

    return True


#  GET, POST operations
@api_view(['GET','POST'])
def list_create_task(request):
    #GET all tasks 
    if request.method == 'GET':
        Tasks = Task.objects.all()
        serializer = TaskSerializer(Tasks, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    #POST a task to the database 
    elif request.method == 'POST':
        serializer = TaskSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)

# GET, PUT, DELETE operations
@api_view(["GET","PATCH","DELETE"])
def get_update_delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    #Get specific task
    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data, status.HTTP_200_OK)
        
    #Update specific task
    if request.method == "PATCH":
        serializer = UpdateTaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(f"Validated data is: {serializer.validated_data}")
        if is_status_changeable(task.status, serializer.validated_data["status"]):
            task.status = serializer.validated_data["status"]
            task.save()
            return Response(serializer.validated_data, status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)

    #Delete specific task
    if request.method == "DELETE":
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
