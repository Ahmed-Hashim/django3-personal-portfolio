from django.shortcuts import render,get_object_or_404
from .models import Port, Project

def home(request):

    projects = Project.objects.all()
    homelogo=Port.objects.all()
    homelogo2 = get_object_or_404(Port, pk=1 )
    return render (request,'portfolio/home.html',{'projects':projects , 'images':homelogo,'image':homelogo2})
