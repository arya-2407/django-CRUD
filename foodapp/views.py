from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.

def index(req):
    return HttpResponse("Hello World")

def item(req):
    item_list = Item.objects.all()
    return render(req,'foodapp/index.html',{'items' : item_list})


def detail(req,item_id):
    item = Item.objects.get(pk=item_id)
    return render(req,'foodapp/detail.html',{'item' : item})
