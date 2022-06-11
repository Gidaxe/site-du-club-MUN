from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *
from toolbox import sort_images
from toolbox.set_defaults import init, init_sliders

def presentation_redirect(request):
    response = redirect('/Presentation/')
    return response


def presentation(request):
    init(PresentationClub)
    init_sliders(BigSlider)
    membres = Membre.objects.all()
    text_presentation = PresentationClub.objects.all()
    sliders = BigSlider.objects.all()
    sliders = sort_images.sort_source(sliders)
    first_slide = sliders[0]
    sliders = BigSlider.objects.exclude(pk=first_slide.pk)
    sliders = sort_images.sort_source(sliders)
    membres = sort_images.sort_source(membres)
    context = {
        'membres': membres,
        'txt_presentation': text_presentation,
        'sliders': sliders,
        'first_slide': first_slide
    }
    template = loader.get_template("Presentation.html")
    return HttpResponse(template.render(context, request))

    # TODO: create generation system to view members, team-up with sasha

