from django import forms
from main.models import Imagen, Producto


class ImagenForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra', None)
        all = kwargs.pop('all', False)
        super(ImagenForm, self).__init__(*args, **kwargs)
        if extra and self.fields.get('producto', None):
            self.fields['producto'].initial = Producto.objects.filter(pk=extra).first()
            if not all:
                self.fields['producto'].queryset = Producto.objects.filter(pk=extra)

    class Meta:
        model = Imagen
        fields = '__all__'
