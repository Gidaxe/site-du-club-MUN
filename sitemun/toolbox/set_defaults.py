'''
{% if  %}

            {% else %}

            {% endif %}
'''


def init(model):
    if not model.objects.all():
        mod = model()
        mod.set_default()
        mod.save()


def init_sliders(model):
    if not model.objects.all():
        for i in range(4):
            mod = model()
            mod.set_default()
            mod.save()
