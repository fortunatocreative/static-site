from django.shortcuts import render

# Create your views here.
## {} are used to pass other python programs into page
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})