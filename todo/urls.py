from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('mark_as_done/<int:task_id>/', views.mark_as_done, name='mark_as_done'),
    path('mark_as_undone/<int:task_id>/', views.mark_as_undone, name='mark_as_undone'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
]

