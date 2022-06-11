from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import TestApp
from django.urls import reverse


def index(request):
    values = TestApp.objects.all().values()
    template = loader.get_template("first.html")
    context = {
        'values': values,
    }
    return HttpResponse(template.render(context, request))


def formpage(request):
    template = loader.get_template("form1.html")
    print('this is the request:' + str(request))
    return HttpResponse(template.render({}, request))


def addobject(request):
    titre0 = request.POST['titre']
    soustitre0 = request.POST['sub']
    piclink0 = request.POST['piclink']
    newobjct = TestApp(titre=titre0, subtitle=soustitre0, piclink=piclink0)
    newobjct.save()
    return HttpResponseRedirect(reverse(index))


def delete(request, id):
    objet = TestApp.objects.get(id=id)
    objet.delete()
    return HttpResponseRedirect(reverse(index))


def modifypage(request, id):
    template = loader.get_template("mod1.html")
    context = {
        'ID': id,
    }
    return HttpResponse(template.render(context, request))


def modify(request, id):
    objet = TestApp.objects.get(id=id)
    titre0 = request.POST['titre']
    soustitre0 = request.POST['sub']
    piclink0 = request.POST['piclink']
    objet.titre = titre0
    objet.subtitle = soustitre0
    objet.piclink = piclink0
    objet.save()
    return HttpResponseRedirect(reverse(index))


def thing(request):
    return HttpResponse("hello my beautiful world")
