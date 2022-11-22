from django.urls import path

from api.views import TaskView, TaskUpdateView

urlpatterns = [
    path('task/<int:pk>', TaskView.as_view(), name='task_view'),
    path('task/update/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
]
