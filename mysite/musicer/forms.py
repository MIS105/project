from django import forms

class nameForm(forms.Form):
    name = forms.CharField()
    sdt = forms.CharField()
    place = forms.CharField()
    website = forms.CharField()