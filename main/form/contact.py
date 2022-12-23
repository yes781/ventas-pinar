from django import forms
from main.models.contact import MyContact


class FormContact(forms.ModelForm):
    class Meta:
        model = MyContact
        fields = ['name', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control input-md'}),
            'email': forms.EmailInput(attrs={'class': 'form-control input-md'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control input-md'})
        }
