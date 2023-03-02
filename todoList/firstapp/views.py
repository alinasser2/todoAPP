from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics



@api_view(["GET"])
def index(request):
    tasks = Task.objects.all()
    task = TaskSerializer(tasks,many=True)
    return Response(task.data)

# pass the task's title and time in a post request to add it
@api_view(["POST"])
def add(request):
    if request.method == "POST":
        task = Task()
        task.time = request.data["time"]
        task.title = request.data["title"]
        task.save()
        return Response(f"{task.time}   {task.title}",status=200)
    return Response("failed",status=200)

# pass id , title and time in an post request. this api determines the considered task with the id then update it's title and time
@api_view(["POST"])
def update(request):
    if request.method == "POST":
        id = request.data["id"]
        title = request.data["title"]
        time = request.data["time"]
        task = Task.objects.get(id = id)
        task.title = title
        task.time = time
        task.save()
    return Response("task updated successfully.",status=200)

# pass the id to delete the task 
@api_view(["POST"])
def delete(request):
    if request.method == "POST":
        id = request.data["id"]
        task = Task.objects.get(id = id)
        task.delete()
        return Response("task deleted successfully.",status=200)



# class based views

# update, get and delete a specific task
class add_delete_update(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'id'

# list all tasks
class ListTasks(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

# add a task
class add_task(generics.CreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()