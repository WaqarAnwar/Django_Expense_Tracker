from django import forms
from django.forms import widgets
from .models import Entry
from datetime import datetime, timezone

class EditForm(forms.ModelForm):
    class Meta:
        model = Entry
        widgets = {
             'date_time' :  forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'})

        }
        fields = ['description', 'amount', 'options', 'date_time']

        def __init__(self, *args, **kwargs):
            super(EditForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                if field.widget.attrs.get('class'):
                    field.widget.attrs['class'] += ' form-control'
                else:
                    field.widget.attrs['class']='form-control'

class AddForm(forms.ModelForm):
    class Meta:
        model = Entry
        widgets = {
             'date_time' :  forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'})
        }
        fields = ['description', 'amount', 'options', 'date_time']

        date_time = forms.DateTimeField(initial=datetime.now(timezone.utc).astimezone().isoformat())

        def __init__(self, *args, **kwargs):
            super(AddForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                if field.widget.attrs.get('class'):
                    field.widget.attrs['class'] += ' form-control'
                else:
                    field.widget.attrs['class']='form-control'


