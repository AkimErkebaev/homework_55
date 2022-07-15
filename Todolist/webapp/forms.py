from django import forms
from django.forms import widgets

from webapp.models import Status, Type, Task


# class TaskForm(forms.Form):
#     name = forms.CharField(max_length=50, required=True, label='Name')
#     description = forms.CharField(max_length=3000, required=False, label='Description',
#                                   widget=widgets.Textarea(attrs={"cols": 40, "rows": 3}))
#     status = forms.ModelChoiceField(queryset=Status.objects.all())
#     types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(),
#                                            required=False, label='Type')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "status", "types"]
        widgets = {
            "types": widgets.CheckboxSelectMultiple,
            "description": widgets.Textarea(attrs={"placeholder": "Введите описание"})
        }
