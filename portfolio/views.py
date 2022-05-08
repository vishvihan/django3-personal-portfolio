from django.shortcuts import render
from .models import Project


def home(request):

    projects = Project.objects.all()
    return render(request,'portfolio/home.html', {'projects':projects})
    

# def contact_me(request):
#     return render(request,'portfolio/contact_me.html')



def projectDetail(request,id):
    project_id = Project.objects.get(id=id)
    return render(request,'portfolio/project_detail.html',{'project_id':project_id})