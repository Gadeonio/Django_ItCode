from django import forms

import core.models

class BookSearch(forms.Form):
    name = forms.CharField(label='Название', required=False)
    min_pages = forms.IntegerField(label='Кол-во страниц', required=False, help_text='Минимальное количество страниц')

    def clean_min_pages(self):
        cleaned_data = self.cleaned_data
        return



class BookEdit(forms.ModelForm):
    class Meta:
        model = core.models.Book
        fields = '__all__'
