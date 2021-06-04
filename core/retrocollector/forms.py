from django import forms
from .models import Collectible


class CollectibleForm(forms.ModelForm):
    class Meta:
        model = Collectible
        fields = '__all__'
        labels = {
            'name': 'Collectible Name'
        }
        widgets = {
            'date_manufactured': forms.DateInput(format=('%d/%m/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(CollectibleForm, self).__init__(*args, **kwargs)
        self.fields['type'].empty_label = 'Select'

