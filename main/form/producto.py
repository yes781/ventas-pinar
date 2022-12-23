from django import forms
from main.models import Producto
from main.models import Categoria


class ProductoForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(Categoria.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control input-md'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control input-md'})
        }
