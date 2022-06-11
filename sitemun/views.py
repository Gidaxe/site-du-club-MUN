from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader


def index():
    template = loader.get_template("index.html")
    print('does somethin')
    return HttpResponse(template.render())


def index_redirect(request):
    response = redirect('/index/')
    return response
