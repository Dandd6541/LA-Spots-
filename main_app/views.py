from django.shortcuts import render 
from django.views.generic.edit import CreateView
from .models import Laspot

# Add the LA SPOTS class & list and view function below the imports

class LaspotCreate(CreateView):
  model = Laspot
  fields = ['name', 'breed', 'description', 'age']

  
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


def laspots_detail(request, laspot_id):
  laspot = Laspot.objects.get(id=laspot_id)
  return render(request, 'laspots/detail.html', { 'laspot': laspot })
