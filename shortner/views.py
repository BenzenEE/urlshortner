from django.shortcuts import render,redirect
import uuid
from django.http import HttpResponse
from .models import Link
# Create your views here.

def index(request):
    return render(request,'home.html')

def val(request):
    if request.method=='POST':
        url = request.POST['url']
        uid = str(uuid.uuid4())[:5]
        ob = Link(url=url,uid=uid)
        ob.save()
        return render(request,'home.html',context={'uid':uid})
    return redirect('index')

def search(request,id):
    ob = Link.objects.get(uid=id)
    return redirect(ob.url)