from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name = "index"),
    path('add/', views.add,name = "add"),
    path('update/', views.update,name = "update"),
    path('delete/', views.delete,name = "delete"),
    path('v2/tasks/<int:id>', views.add_delete_update.as_view()),
    path('v2/list', views.ListTasks.as_view()),
    path('v2/add', views.add_task.as_view())
]