from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from tracker.forms import AddEditForm
from tracker.models.issue_tracker import IssueTracker


class EditView(UpdateView):
    template_name = "edit_task.html"
    form_class = AddEditForm
    model = IssueTracker
    success_url = reverse_lazy('main')
    context_object_name = 'article'
