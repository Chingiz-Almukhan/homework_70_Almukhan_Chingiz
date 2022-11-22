from django.urls import path

from api.views import TaskView
from tracker.views.base import IndexView

urlpatterns = [
    path('task/<int:pk>', TaskView.as_view(), name='task_view'),
]
