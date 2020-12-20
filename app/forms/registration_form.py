from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app.models.extend_user import ExtendUser


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Optional'}),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name', False)
        if not first_name:
            raise forms.ValidationError('First name is required')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name', False)
        if not last_name:
            raise forms.ValidationError('Last name is required')
        return last_name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserExtendForm(forms.ModelForm):
    class Meta:
        model = ExtendUser
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
