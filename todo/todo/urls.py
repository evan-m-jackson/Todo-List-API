"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from api.views import *

urlpatterns = [
    path('api', apiOverview, name="api-overview"),
    path('todo-list/', taskList, name="task-list"),
    path('todo-detail/<str:pk>', taskDetail, name="task-Detail"),
    path('todo/<str:pk>', taskUpdate, name="task-update"),
    path('todo', taskCreate, name="task-Create"),
    path('todo-delete/<str:pk>', taskDelete, name="task-delete"),
    path('todo-ids', firstTaskID, name="task-ids"),
  ]