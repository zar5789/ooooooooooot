
from unicodedata import category
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import stock

from django.urls import reverse


def index(request):
    mystock = stock.objects.all().values()
    template = loader.get_template('myfirst.html')
    context = {
        'stock' : mystock
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    name = request.POST['name']
    category = request.POST['category']
    brand = request.POST['brand']
    qty = request.POST['qty']
    price = request.POST['price']
    picture = request.POST['picture']
    update = stock(Product_name=name, Category=category, brand_name=brand, qty=qty, price=price, picture=picture)
    update.save()
    return HttpResponseRedirect(reverse('index'))

def search_record(request):
    sname = request.GET['sname']
    scate = request.GET['scate']
    sbr = request.GET['sbr']
    search_result = stock.objects.filter(Product_name__icontains=sname, Category__icontains=scate, brand_name__icontains=sbr)
    template = loader.get_template('search.html')
    context = {
        'stock' : search_result
    }
    return HttpResponse(template.render(context, request))

def edit(request, id):
    item = stock.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'stock': item,
    }
    return HttpResponse(template.render(context, request))

def edit_record(request, id):
    name = request.POST['name']
    category = request.POST['cate']
    brand = request.POST['brand']
    qty = request.POST['qty']
    price = request.POST['price']
    picture = request.POST['picture']
    item = stock.objects.get(id=id)
    item.Product_name = name
    item.Category = category
    item.brand_name = brand
    item.qty = qty
    item.price = price
    item.picture = picture
    item.save()
    return HttpResponseRedirect(reverse('index'))

def remove_record(request, id):
    item = stock.objects.get(id = id)
    item.delete()
    return HttpResponseRedirect(reverse('index'))

def back_main(request):
    return HttpResponseRedirect(reverse('index'))