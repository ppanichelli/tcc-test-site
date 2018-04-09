from django.shortcuts import render, redirect
from .forms import NewProjectForm
from .models import Project, Well

# Create your views here.
def home(request):
    return render(request, 'home.html')

def new_project(request):
    if request.method == 'POST':
        form = NewProjectForm(request.POST) # Instantiate the form from the POST data.
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('home')
    else:
         form = NewProjectForm()

    return render(request, 'new-project.html', {'form': form})

def injections(request):
    project = Project.objects.get(pk=1)
    return render(request, 'new-project.html', {'project': project})