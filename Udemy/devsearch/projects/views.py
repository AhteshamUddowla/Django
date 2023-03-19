from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
projctsList = [
    {
        'id':'1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
     {
        'id':'2',
        'title': 'Portfolio Website',
        'description': 'Fully functional portfolio website'
    },
     {
        'id':'3',
        'title': 'Social Network',
        'description': 'Fully functional social network'
    }
]

def projects(request):
    page = "projects"
    number = 10
    context = {
        "page": page,
        "number": number,
        "projects": projctsList,
    }
    return render(request, 'projects/projects.html', context)

def project(request,pk):
    projectobj = None
    for i in projctsList:
        if i['id'] == pk:
            projectobj = i
    return render(request, 'projects/single-project.html', {'project': projectobj})