from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .models import *
from toolbox.set_defaults import init

def sort_source(container):
    if container.img_url1 and not container.img_upload1:
        container.img_url1 = container.img_url1
    elif container.img_upload1 and not container.img_url1:
        container.img_url1 = container.img_upload1.url
    elif not container.img_upload1 and not container.img_url1:
        container.img_url1 = '/static/images/grntriangles.jpg'
    else:
        container.img_url1 = container.img_upload1.url

    if container.img_url2 and not container.img_upload2:
        container.img_url2 = container.img_url2
    elif container.img_upload2 and not container.img_url2:
        container.img_url2 = container.img_upload2.url
    elif not container.img_upload2 and not container.img_url2:
        container.img_url2 = '/static/images/grntriangles.jpg'
    else:
        container.img_url2 = container.img_upload2.url

    if container.img_url3 and not container.img_upload3:
        container.img_url3 = container.img_url3
    elif container.img_upload3 and not container.img_url3:
        container.img_url3 = container.img_upload3.url
    elif not container.img_upload3 and not container.img_url3:
        container.img_url3 = '/static/images/grntriangles.jpg'
    else:
        container.img_url3 = container.img_upload3.url


def index(request):
    init(AccueilIntroMun)

    intro_mun = AccueilIntroMun.objects.last()

    sort_source(intro_mun)

    context = {
        'x': intro_mun
    }
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))


def index_redirect(request):
    response = redirect('/index/')
    return response
