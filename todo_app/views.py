from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import todoitems

# Create your views here.
def index(request):
    all_items = todoitems.objects.all
    params = {"all_items":all_items}
    return render(request, "index.html", params)

def add(request):
    item = request.POST.get("content")
    new_item = todoitems(content = item)
    new_item.save()
    return HttpResponseRedirect("/")

def delete(request, todo_id):
    item_to_delete = todoitems.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect("/")