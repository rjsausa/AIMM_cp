from django.shortcuts import render

def project_list(req):
    return render(req, 'aimm/project-list.html')

def project_detail(req, project_slug):
    return render(req, 'aimm/project-detail.html')

