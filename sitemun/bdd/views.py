from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *
from toolbox import sort_images


def bdd(request):
    template = loader.get_template("BDD.html")
    files = BddFile.objects.all()
    sort_images.sort_source(files)
    context = {
        'files': files,
    }
    return HttpResponse(template.render(context, request))


def bdd_redirect(request):
    response = redirect('/BDD/')
    return response

#TODO create a search engine
