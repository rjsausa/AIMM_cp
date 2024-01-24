from django.shortcuts import render, get_object_or_404
from .models import Project
from django.views.generic import CreateView

def project_list(req):
    return render(req, 'aimm/project-list.html')

def project_detail(req, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    return render(req, 'aimm/project-detail.html', {'project':project, 'expense_list': project.expenses.all()'})

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'aimm/add-project.html'
    fields = ('name', 'budget')
