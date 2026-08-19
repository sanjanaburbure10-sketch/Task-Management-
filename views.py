from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Task


@login_required
def home(request):

    tasks = Task.objects.filter(user=request.user)

    total_tasks = tasks.count()
    pending_tasks = tasks.filter(status="Pending").count()
    completed_tasks = tasks.filter(status="completed").count()

    return render(
        request,
        "taskapp/index.html",
        {
            "tasks": tasks,
            "total_tasks": total_tasks,
            "pending_tasks": pending_tasks,
            "completed_tasks": completed_tasks,
        }
    )


@login_required
def add_task(request):

    if request.method == "POST":

        title = request.POST["title"]
        description = request.POST["description"]
        due_date = request.POST["due_date"]
        status = request.POST["status"]

        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            due_date=due_date,
            status=status
        )

        return redirect("home")

    return render(
        request,
        "taskapp/add_task.html"
    )


@login_required
def edit_task(request, task_id):

    task = Task.objects.get(
        id=task_id,
        user=request.user
    )

    if request.method == "POST":

        task.title = request.POST["title"]
        task.description = request.POST["description"]
        task.due_date = request.POST["due_date"]
        task.status = request.POST["status"]

        task.save()

        return redirect("home")

    return render(
        request,
        "taskapp/edit_task.html",
        {"task": task}
    )


@login_required
def delete_task(request, task_id):

    task = Task.objects.get(
        id=task_id,
        user=request.user
    )

    if request.method == "POST":

        task.delete()

        return redirect("home")

    return render(
        request,
        "taskapp/delete_task.html",
        {"task": task}
    )


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            return render(
                request,
                "registration/register.html",
                {"error": "Username already exists. Please choose another username."}
            )

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect("home")

    return render(request, "registration/register.html")