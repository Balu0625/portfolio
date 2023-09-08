"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from demoapp.views import *
from django.conf.urls.static import static
from django.conf import  settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name='home'),
    path("services/rockpaper",rockpaper,name='rockpaper'),
    #path("services/ser1/",ser1,name='ser1'),
    path("services/ser2/",ser2,name='ser2'),
    path("services/ser2/moviere",moviere,name='moviere'),
    path("services/",services,name='services'),
    path("services/ser3/",ser3,name='ser3'),
    
    path("services/ser3/diary",diary,name='diary'),
    
    path("services/diary/entries",entries,name='entries'),
    path("services/diary/entries/delete_entry/<entry_id>/",delete_entry,name='delete_entry'),
    path("about/",about,name='about'),
    path("contact/",contact,name='contact'),
    path("contact/submitted/",submitted,name='submitted'),

    path("services/todo",todo,name='todo'),
    path('services/todo/add_todo/',add_todo, name='add_todo'),
    path('services/todo/edit/<int:todo_id>/', edit_todo, name='edit_todo'),
    path('services/todo/delete/<int:todo_id>/', delete_todo, name='delete_todo'),
    path('services/todo/toggle/<int:todo_id>/', toggle_todo, name='toggle_todo'),
]


urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)