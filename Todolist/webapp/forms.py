from django import forms
from django.forms import widgets


class TaskForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label='Name')
    status = forms.CharField(max_length=50, required=True, label='Status')
    description = forms.CharField(max_length=3000, required=True, label='Description',
                                  widget=widgets.Textarea(attrs={"cols": 40, "rows": 3}))
