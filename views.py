from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from todo.models import todo_list
# Create your views here.


def home(request):
    if request.method == "POST":
        title_temp=request.POST.get("title")
        if title_temp:
            items=todo_list(title=title_temp)
            items.save()
    data=todo_list.objects.all()
    return render(request,'todo-home.html',{
        'data':data,
    })

def update_todo(request,id):
    item=todo_list.objects.get(id=id)
    item.check_status = not item.check_status
    item.save()
    return HttpResponseRedirect(reverse('homepage'))

def delete_todo(reqest,id):
    item = todo_list.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect(reverse('homepage'))
        