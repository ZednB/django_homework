from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_name = self.cleaned_data['name']
        prohibited_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                           'бесплатно', 'обман', 'полиция', 'радар']
        for word in prohibited_word:
            if word.lower() not in cleaned_name.lower():
                return cleaned_name
            raise forms.ValidationError(f"В названии запрещенное слово - {word}")

    def clean_description(self):
        cleaned_name = self.cleaned_data['description']
        prohibited_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                           'бесплатно', 'обман', 'полиция', 'радар']
        for word in prohibited_word:
            if word.lower() not in cleaned_name.lower():
                return cleaned_name
            raise forms.ValidationError(f"В описании запрещенное слово - {word}")
