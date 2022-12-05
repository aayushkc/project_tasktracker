
import email
from multiprocessing import context
from re import template
from django.shortcuts import redirect, render
from .forms import TaskCreateForm, LoginForm, RegisterForm
from .models import AppUser, Task
from django.core.mail import send_mail
# Create your views here.
def task_index(request):
    if request.session.has_key('session_email'):

        tasks = Task.objects.all() # return whole list of data dict
        context = {
            "title":"Task Create",
            "body_title":"Task Create | Task Tracker",
            "tasks": tasks
        }
        template = "tasks/index.html"
        return render(request, template, context)
    else:
        return redirect('user.login')

def task_update(request):
    if request.method == 'POST':
        task = Task.objects.get(id=request.POST.get('id'))
        task.task_title = request.POST.get('task_title')
        task.task_desc = request.POST.get('task_desc')
        task.task_category = request.POST.get('task_category')
        task.task_assign_to= request.POST.get('task_assign_to')
        task.task_assigned_by = request.POST.get('task_assigned_by')
        task.task_end_date = request.POST.get('task_end_date')
        task.task_assign_date = request.POST.get('task_assign_date')
        task.save()
        tasks = Task.objects.all() # return whole list of data dict
        context = {
        "title":"Task Create",
        "body_title":"Task Create | Task Tracker",
        "tasks": tasks
    }
        template = 'tasks/index.html'
        return render(request, template, context)
    else:
        create_form = TaskCreateForm()
        template = "tasks/create.html"
        context = {
            "title":"Task Create",
            "body_title":"ToDo APP | Task Create",
            "form": create_form
        }
        return render(request, template, context)

def task_edit(request, id):
    task = Task.objects.get(id=id)
    context = {
        "title":"Task Create",
        "body_title":"Task Create | Task Tracker",
        "task": task
    }
    template = "tasks/edit.html"
    return render(request, template, context)

def task_show(request, id):
     task = Task.objects.get(id = id)
     context = {
        "title":"Task Create",
        "body_title":"Task Create | Task Tracker",
        "task": task
     }
     template = "tasks/show.html"
     return render(request, template, context)

def task_delete(request, id):
    task = Task.objects.get(id = id)
    task.delete() # delete the task
    task = Task.objects.all()
    context = {
        "title":"Task Create",
        "body_title":"Task Create | Task Tracker",
        "tasks": task
     }
    template = "tasks/index.html"
    return render(request, template, context)

def task_create(request):

    if request.method == 'POST':
        # task = Task()
        # task.task_title = request.POST.get('task_title')
        # task.task_desc = request.POST.get('task_desc')
        # task.task_category = request.POST.get('task_category')
        # task.task_assign_to= request.POST.get('task_assign_to')
        # task.task_assigned_by = request.POST.get('task_assigned_by')
        # task.task_end_date = request.POST.get('task_end_date')
        # task.task_assign_date = request.POST.get('task_assign_date')
        # task.save()
        form_data = TaskCreateForm(request.POST, request.FILES)
        if form_data.is_valid():
            form_data.save()
            send_mail(
                'Task Assignment:' + request.POST.get('task_title'),
                'You are assigned to a task, Task Assign date:' + str( request.POST.get('task_assign_date')),
                'summerboyaayush@gmail.com',
                [request.POST.get('task_assign_to')]
            )
            return redirect('task.index')
        else:
            return redirect('task.create')
        # send_mail(
        #     'Task Assignment:' + task.task_title,
        #     'You are assigned to a task, Task Assign date:' + str(task.task_assign_date),
        #     'summerboyaayush@gmail.com',
        #     [task.task_assign_to]
        # )
    else:
        create_form = TaskCreateForm()
        template = "tasks/create.html"
        context = {
            "title":"Task Create",
            "body_title":"ToDo APP | Task Create",
            "form": create_form
        }
        return render(request, template, context)

def user_login(request):
    if request.method == 'POST':
        req_email = request.POST.get('email')
        req_password = request.POST.get('password')
        db_data = AppUser.objects.get(email=req_email)
        if req_password == db_data.password:
            request.session.setdefault('session_email', db_data.email)
            return redirect('task.index')
        else:
            return redirect('user.login')
        # return redirect('task.list')
    else:
        login_form = LoginForm()
        template = 'users/login.html'
        context = {
            'form': login_form
        }
        return render(request, template,context)


def user_register(request):
    if request.method == "POST":
        form_data = RegisterForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            request.session.setdefault('session_email', request.POST.get('email'))
            return redirect('task.index')
        else:
            return redirect('user.register')
    else:
        reg_form = RegisterForm()
        template = 'users/register.html'
        context = {'form':reg_form}
        return render(request,template,context)
def user_logout(request):
    if request.session.has_key('session_email'):
        del request.session['session_email']
        return redirect('user.login')
    else:
        return redirect('user.login')