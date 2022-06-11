from django import template
from presentation.models import Membre

register = template.Library()

@register.simple_tag
def update_gens():
    pass
