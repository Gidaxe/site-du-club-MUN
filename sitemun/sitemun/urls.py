"""sitemun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#faites pas attention au rouge, python est juste stupide...

import admin
from django.urls import path, include
from index import views as v_index
from presentation import views as v_pres
from actus import views as v_actus
from bdd import views as v_bdd
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('testapp/', include('testapp.urls')),
    path('admin/', admin.site.urls),

    path("", v_index.index),
    path("index/", v_index.index),
    path("Presentation/", v_pres.presentation),
    path("Actus/", v_actus.actus),
    path("BDD/", v_bdd.bdd),
    path("login/", admin.site.urls),

    path("index/index/", v_index.index_redirect),
    path("index/Presentation/", v_pres.presentation_redirect),
    path("index/Actus/", v_actus.actus_redirect),
    path("index/BDD/", v_bdd.bdd_redirect),
    path("index/login/", admin.site.urls),

    path("Presentation/index/", v_index.index_redirect),
    path("Presentation/Presentation/", v_pres.presentation_redirect),
    path("Presentation/Actus/", v_actus.actus_redirect),
    path("Presentation/BDD/", v_bdd.bdd_redirect),
    path("Presentation/login/", admin.site.urls),

    path("Actus/index/", v_index.index_redirect),
    path("Actus/Presentation/", v_pres.presentation_redirect),
    path("Actus/Actus/", v_actus.actus_redirect),
    path("Actus/BDD/", v_bdd.bdd_redirect),
    path("Actus/login/", admin.site.urls),

    path("BDD/index/", v_index.index_redirect),
    path("BDD/Presentation/", v_pres.presentation_redirect),
    path("BDD/Actus/", v_actus.actus_redirect),
    path("BDD/BDD/", v_bdd.bdd_redirect),
    path("BDD/login/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Section Administration"
admin.site.index_title = ""
admin.site.site_title = ""
