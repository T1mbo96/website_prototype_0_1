from django import forms

from .models import SearchQuery


class SearchForm(forms.ModelForm):

    class Meta:
        model = SearchQuery
        fields = ('state', 'place', 'zip', 'street', 'house_number')
