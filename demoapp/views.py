from django.shortcuts import render,redirect
from django.http import HttpResponse
from demoapp.movie import *
from .models import *
from django.contrib import messages
import datetime
from django.views.decorators.csrf import csrf_exempt





#from django.views.decorators.csrf import csrf_protect
# import requests
# from bs4 import BeautifulSoup



def home(request):
    return render(request,"home.html")

# def ser1(request):
#     return render(request,"ser1.html")

def ser2(request):
    return render(request,"ser2.html")

def ser3(request):
    return render(request,"ser3.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def rockpaper(request):
    return render(request,"rockpaper.html")


def services(request):
    return render(request,"services.html")


@csrf_exempt
def todo(request):
    todos = Todo.objects.all()
    return render(request, 'todo.html', {'todos': todos})


@csrf_exempt
def submitted(request):
    cont=Details(name=request.POST.get('name'),
         email=request.POST.get('email'),
         sub=request.POST.get('subject'))
    cont.save()

    return render(request,"submitted.html",{'name':request.POST.get('name'),'email':request.POST.get('email'),'sub':request.POST.get('subject')})




#@csrf_protect
def add(request):
    a=int(request.GET['num1'])
    b=int(request.GET['num2'])
    c=a+b
    
    return render(request,"result.html",{'key':c})

def moviere(request):
    genres=request.GET['genres']
    print(genres)
    genres = genres.split()
    print(genres)
    
    recommended_movies = get_movies_by_genre(genres)
    for m in recommended_movies:
        m['cast']=[item.replace('\n','').replace('|'," ").replace('Stars','') for item in m['cast']]
    for m in recommended_movies:
        print(m['cast'])
    
    return render(request,"exp.html",{"gen":recommended_movies})
    



def diary(request):
    
    if 'diary-entry' in request.GET and request.GET['diary-entry']!="":
            entry_content = request.GET['diary-entry']
            current_datetime = datetime.datetime.now()
            current_date = current_datetime.date()
            current_time = current_datetime.time()
            current_day = current_datetime.strftime('%A')
            new_entry = Diary(diary=entry_content,date=current_date,time=current_time,day=current_day)
            new_entry.save()
    
    diary_entries = Diary.objects.all()  # Fetch all diary entries from the database
    
    return render(request, "ser3.html", {'diary_entries': diary_entries})
    
    
    



@csrf_exempt
def add_todo(request):
    if request.method == 'POST':
        task = request.POST['task']
        Todo.objects.create(task=task)
    return redirect('todo')

def edit_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        task = request.POST['task']
        todo.task = task
        todo.save()
        return redirect('todo')
    return render(request, 'edit_todo.html', {'todo': todo})

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo')

def toggle_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo')


def entries(request):
    entry=Diary.objects.all()
    
    return render(request,"entries.html",{"entry":entry})


def delete_entry(request, entry_id):
    try:
        
        entry = Diary.objects.get(pk=entry_id)
        
        entry.delete()
        entry=Diary.objects.all()
        return render(request,"entries.html",{"entry":entry})
    except Diary.DoesNotExist:

        return render(request,"entries.html",{"entry":0})

    
    
        
         
