from django.shortcuts import render, HttpResponse, redirect
from .models import *
# Create your views here.
# Homepage

# Show.objects.all().delete()
# print(Show.objects.all())

def index(request):
    context={
        "all_shows": Show.objects.all()
    }   
    return render(request, "shows/index.html", context)


def add_show(request):
    return render(request, "shows/add_show.html" )


def submit_show(request):
    print(request.POST)
    Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
    return redirect("/shows")

def display_show(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, "shows/display_show.html", context)

def edit_show(request, id):
    context = {
        "show": Show.objects.get(id=id),
        "date": str(Show.objects.get(id=id).release_date)
    }
    return render(request, "shows/edit_show.html", context)

def submit_edit(request, id):
    selected = Show.objects.get(id=id)
    if request.POST['title']:
        selected.title = request.POST['title']
    
    if request.POST['network']:
        selected.network = request.POST['network']
    
    if request.POST['release_date']:
        selected.release_date = request.POST['release_date']
    
    if request.POST['description']:
        selected.description = request.POST['description']
    selected.save()
    return redirect("/shows")

def delete_show(request, id):
    Show.objects.get(id=id).delete()
    return redirect("/shows")