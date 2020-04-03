from django.shortcuts import render
from django.http import HttpResponse
from .models import UserDatabase, ItemDatabase
from .forms import NewUserForm, NewItemForm

# Create your views here.

def index(request):

    return render(request, 'skeleton/index.html')

def signup(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'skeleton/signup.html', {'user_form':form})

def database(request):
    form = NewItemForm()

    if request.method == "POST":
        form = NewItemForm(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    items = ItemDatabase.objects.all()

    return render(request, 'skeleton/database.html', {'items':items, 'item_form':form})
