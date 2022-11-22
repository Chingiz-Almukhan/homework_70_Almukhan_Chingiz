from django.urls import path

from api.views import TaskView, TaskUpdateView, DeleteTaskView, ProjectView

urlpatterns = [
    path('task/<int:pk>', TaskView.as_view(), name='task_view'),
    path('task/update/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
    path('task/delete/<int:pk>', DeleteTaskView.as_view(), name='task_delete'),
    path('project/<int:pk>', ProjectView.as_view(), name='project_view')
]
