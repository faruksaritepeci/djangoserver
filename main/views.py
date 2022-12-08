from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def root(responese):
    return redirect("/home")

def home(response):
    return render(response, "main/home.html", {})

def index(response, id):
    if not response.user.is_authenticated:
        return redirect("/login")
    if not response.user.todolist_set.filter(id=id):
        return redirect("/view")
    ls = ToDoList.objects.get(id=id)
    
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.completed = True
                else:
                    item.completed = False
                
                item.save()
            
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) > 2 and len(txt) < 250:
                ls.item_set.create(text=txt, completed=False)
            else:
                print("invalid input for: add new task")
    

    return render(response, "main/list.html", {"ls": ls})

def create(response: HttpRequest):
    if not response.user.is_authenticated: return redirect("/login")
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = response.user.todolist_set.create(name=n)
        
            return HttpResponseRedirect(f"/%i" %t.id)
        else: return redirect("/create")
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})

def view(response: HttpRequest):
    return render(response, "main/view.html", {})


def redirectHome(response):
    return redirect("/home")
