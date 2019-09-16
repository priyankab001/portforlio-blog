from django.shortcuts import render
from .models import Project
# Create your views here.

def project_index(request):
    # In this case, you’re retrieving all objects in the projects table.
    # A database query returns a collection of all objects that match the query, known as a Queryset. In this case, you want all objects in the table, so it will return a collection of all projects.
    projects = Project.objects.all() 
    #The context dictionary is used to send information to our template. 
    # Every view function you create needs to have a context dictionary.
    context = {'projects':projects}
    return render(request,'project_index.html',context)

def project_detail(request,id):
    project=Project.objects.get(id=id)
    context = {'project':project}    
    return render(request,"project_detail.html",context)