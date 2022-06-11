from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path('app/', views.thing),
    path("form1/", views.formpage),
    path("form1/addobject/", views.addobject),
    path("delete/<int:id>", views.delete),
    path("modify/<int:id>", views.modifypage),
    path("modify/modobject/<int:id>", views.modify)
]
