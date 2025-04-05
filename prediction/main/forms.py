from django import forms
from .models import PricePrediction

class PricePredictionForm(forms.ModelForm):
    class Meta:
        model = PricePrediction
        fields = ['surface_area', 'latitude', 'longitude', 'neighborhood']
        widgets = {
            'surface_area': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter surface area in m²',
            }),
            'latitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 'any',
                'placeholder': 'Enter latitude',
            }),
            'longitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 'any',
                'placeholder': 'Enter longitude',
            }),
            'neighborhood': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
