from index.models import *
from actus.models import *
from general.models import *
from toolbox.set_defaults import init


def footer_datta(request):
    init(Footer)
    foot = Footer.objects.last()
    return {'foot': foot}


def img_news_box_datta(request):
    datta = NewsBox.objects.last()
    return {'img_news_box': datta}


def background(request):
    init(Background)
    datta = Background.objects.last()
    return {'background': datta}


def navbar(request):
    init(NavBar)
    datta = NavBar.objects.last()
    return {'navbar': datta}


def generation(request):
    init(Generation)
    datta = Generation.objects.last()
    return {'home': datta}
