from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Status, Type, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "status", "types"]
        widgets = {
            "types": widgets.CheckboxSelectMultiple,
            "description": widgets.Textarea(attrs={"placeholder": "Введите описание"})
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) > 7:
            raise ValidationError("Название должно быть  короче 7 символов")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if len(description) < 5:
            raise ValidationError("Название не должно быть  короче 5 символов")
        return description


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Найти')
