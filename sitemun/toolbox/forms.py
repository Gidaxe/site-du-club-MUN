from django import forms
from presentation.models import Membre
from general.models import Generation


class MemberForm(forms.ModelForm):
    generation = forms.ModelChoiceField(queryset=Generation.objects.all())

    class Meta:
        model = Membre
        fields = [
            'img_url',
            'img_upload',
            'generation',
            'Nom',
            'description_perso',
        ]

