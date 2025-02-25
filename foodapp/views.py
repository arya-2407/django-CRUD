from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
# Create your views here.

def index(req):
    return HttpResponse("Hello World")

def item(req):
    item_list = Item.objects.all()
    return render(req,'foodapp/index.html',{'items' : item_list})


def detail(req,item_id):
    item = Item.objects.get(pk=item_id)
    return render(req,'foodapp/detail.html',{'item' : item})

def create_item(req):
    form = ItemForm(req.POST or None)
    if form.is_valid():
        form.save()
        return redirect('foodapp:item')
    return render(req,'foodapp/item-form.html',{'form':form})

def update_item(req,item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(instance=item)
    if req.method == 'POST':
        form = ItemForm(req.POST,instance=item)
        if form.is_valid():
            form.save()
        return redirect('foodapp:item')
    return render(req,'foodapp/item-form.html',{'form':form, 'item' : item})