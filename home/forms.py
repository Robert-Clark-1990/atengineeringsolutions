from django import forms
from .models import Reviews


class ReviewsForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-5'
