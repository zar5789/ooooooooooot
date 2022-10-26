from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import stock


def index(request):
    mystock = stock.object.all().value()
    template = loader.get_template("myfirst.html")
    context = {'mystock' : mystock}
    return HttpResponse(template.render(context, request))
