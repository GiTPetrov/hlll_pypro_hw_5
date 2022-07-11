from django import forms


class TriangleForm(forms.Form):
    leg_one = forms.IntegerField(label='leg 1', min_value=1, max_value=30, required=True)
    leg_two = forms.IntegerField(label='leg 2', min_value=1, max_value=30, required=True)
