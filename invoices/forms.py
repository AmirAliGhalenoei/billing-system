from django import forms


class CreateinvoiceItemForm(forms.Form):
    title = forms.CharField(max_length=256)
    quantity = forms.IntegerField(min_value=1)
    price = forms.IntegerField(min_value=0)
    discount = forms.IntegerField(required=False, min_value=0, max_value=100)