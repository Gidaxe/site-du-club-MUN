from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *


def actus(request):
    boxes = NewsBox.objects.all()
    context = {
        'Boxes': boxes,

    }
    template = loader.get_template("Actus.html")

    return HttpResponse(template.render(context, request))


def actus_redirect(request):
    response = redirect('/Actus/')
    return response

    # TODO: customizable default image
    # TODO: ask sasha to do a customizable size system
