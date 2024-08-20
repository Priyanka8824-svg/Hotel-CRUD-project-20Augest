from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Hotel
from .forms import HotelForm

# Create your views here.
def homeview(request):
    return render(request,"app1/home.html",{})
def addview(request):
    form = HotelForm()
    if request.method == "POST":
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request,"app1/add_order.html",{"form":form})
def showview(request):
    menu = Hotel.objects.all()
    print(menu)
    return render(request,"app1/show_order.html",{"obj":menu})
def updateview(request, pk):
    obj = Hotel.objects.get(hid=pk)
    form = HotelForm(instance=obj)
    if request.method == 'POST':
        form = HotelForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request,"app1/add_order.html",{"form":form})

def deleteview(request, x):
## directly delete record
  #  obj = Hotel.objects.get(hid=x)
  # obj.delete()
  #  return redirect('/a1/sv/')

#confirm page
    obj = Hotel.objects.get(hid=x)
    if request.method == "POST":
        obj.delete()
        return redirect('/a1/sv/')
    return render(request,"app1/success.html",{"obj":obj})
