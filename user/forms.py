from django import forms
from .models import Film


class FindForm(forms.Form):
    fname = forms.ModelChoiceField(
        queryset=Film.objects.all(),
        to_field_name="slug",
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Фильм'
    )