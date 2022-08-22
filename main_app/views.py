from django.shortcuts import render 
from .models import Laspot

# Add the Cat class & list and view function below the imports

  
# Define the home view
def home(request):
  return render(request, 'home.html')
# Create your views here.
def about(request):
  return render(request, 'about.html')

# Add new view

def laspots_index(request):
  laspots = Laspot.objects.all()
  return render(request, 'laspots/index.html', { 'laspots': laspots })

