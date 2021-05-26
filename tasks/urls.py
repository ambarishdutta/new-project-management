from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="list"),
    path('add_task/', views.addTask, name="add_task"),
    path('add_taskWork/<str:pk>/', views.addTaskWork, name="add_taskWork"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('update_taskWork/<str:pk>/', views.updateTaskWork, name="update_taskWork"),
    path('view/<str:pk>/', views.viewProject, name="view"),
    path('delete/<str:pk>/', views.deleteTask, name="delete")
]
