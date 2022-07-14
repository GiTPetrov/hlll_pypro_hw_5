from django import forms

from triangle.models import Person


class TriangleForm(forms.Form):
    leg_one = forms.IntegerField(label='leg 1', min_value=1, required=True)
    leg_two = forms.IntegerField(label='leg 2', min_value=1, required=True)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
