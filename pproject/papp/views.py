from django.shortcuts import render
from . models import place


from django.shortcuts import render

def fun(request):
    obj=place.objects.all()
    return render(request,"index.html",{'result':obj})