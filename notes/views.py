from django.shortcuts import render
from .models import Note
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    tasks = Note.objects.all()
    context = {"tasks":tasks}
    return render(request,'notes/index.html',context)

def add(request):
    try:
        task = Note(task = request.POST['task'])
    except:
        return HttpResponseRedirect(reverse('notes:index'),{"error": "algo fallo"})
    else:
        task.save()
        return HttpResponseRedirect(reverse('notes:index'),{"error":"guardado"})

def remove(request):
    try:
        dones = request.POST.getlist('done')
    except:
        return HttpResponseRedirect(reverse('notes:index'),{"error":"fallamos"})
    else:
        for d in dones:
            note = Note.objects.get(id=d)
            note.delete()
        return HttpResponseRedirect(reverse('notes:index'),{"error":"listo"})
