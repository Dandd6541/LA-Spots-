from django.shortcuts import render 
from .models import Laspot

# Add the Cat class & list and view function below the imports
class Laspot:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

laspots_index = [
  Laspot('Lolo', 'tabby', 'foul little demon', 3),
  Laspot('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Laspot('Raven', 'black tripod', '3 legged cat', 4)
]

def laspots_index(request):
  laspots = Laspot.objects.all()
  return render(request, 'laspots/index.html', { 'laspots': laspots })
  
# Define the home view
def home(request):
  return render(request, 'home.html')
# Create your views here.
def about(request):
  return render(request, 'about.html')

# Add new view


