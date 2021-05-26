from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html', context)

def viewProject(request, pk):
    task = Task.objects.get(id=pk)
    # taskWork = TaskWork.objects.filter(project=pk).values('taskleft')
    taskWork = TaskWork.objects.filter(project=pk)
    print("*****: ",taskWork)
    context = {'task':task, 'taskWork':taskWork}
    print("Context: ",context)
    return render(request, 'tasks/viewProject.html', context)

def addTask(request):
    # task = Task.objects.get(id=pk)
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {'form':form}
    # context = {'tasks':tasks}
    return render(request, 'tasks/add.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {'form':form}
    return render(request, 'tasks/add.html', context)

def addTaskWork(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskWorkForm(initial={'project':task})
    if request.method == 'POST':
        print(request.POST)
        form = TaskWorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {'form':form}
    return render(request, 'tasks/addTaskWork.html', context)

def updateTaskWork(request, pk):
    task = TaskWork.objects.filter(project=pk).first()
    form = TaskWorkForm(instance=task)
    if request.method == 'POST':
        form = TaskWorkForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("add_task")
    context = {'form':form}
    return render(request, 'tasks/addTaskWork.html', context)

# def updateTask(request, pk):
#     task = Task.objects.get(id=pk)
#     form = TaskForm(instance=task)
#     if request.method == 'POST':
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#
#     context = {'form': form}
#     return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'tasks/delete.html', context)
