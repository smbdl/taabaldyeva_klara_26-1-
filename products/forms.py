from django import forms


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=True)
    title = forms.CharField(max_length=255, min_length=6)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.FloatField(required=True)
    rate = forms.FloatField(required=False)


class ReviewCreateForm(forms.Form):
    text = forms.CharField(max_length=255, min_length=3)
