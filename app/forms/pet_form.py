from django import forms

from app.models.Pet import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
