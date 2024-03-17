from django import forms
from catalog.models import Product, Version


class StyleFormsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormsMixin, forms.ModelForm):
    prohibited_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                       'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_name = self.cleaned_data['name']

        for word in self.prohibited_word:
            if word.lower() not in cleaned_name.lower():
                return cleaned_name
            raise forms.ValidationError(f"В названии запрещенное слово - {word}")

    def clean_description(self):
        cleaned_name = self.cleaned_data['description']
        for word in self.prohibited_word:
            if word.lower() not in cleaned_name.lower():
                return cleaned_name
            raise forms.ValidationError(f"В описании запрещенное слово - {word}")


class VersionForm(StyleFormsMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
