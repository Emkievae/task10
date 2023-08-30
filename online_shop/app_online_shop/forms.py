from django import forms
from .models import OnlineShop
from django.core.exceptions import ValidationError

class AdvertisementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['description'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['image'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['price'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['auction'].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = OnlineShop
        fields = ("title", "description", "image", "price", "auction")

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise ValidationError('Заголовок не может начинаться с вопросительного знака')
        return title