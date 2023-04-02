from django.urls import path
from .views import TaskList,TaskDetail,AddTask,UpdateTask,DeleteTask,CustomLoginView,RegisterPage

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/',RegisterPage.as_view(),name='register'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page="login"),name='logout'),
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>',TaskDetail.as_view(),name ='task'),
    path('add-task',AddTask.as_view(),name='add-task'),
    path('update-task/<int:pk>',UpdateTask.as_view(),name='update-task'),
    path('delete-task/<int:pk>',DeleteTask.as_view(),name='delete-task'),
]

