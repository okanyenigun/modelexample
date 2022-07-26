from django.forms import ModelForm
from .models import Sales, Salesmen

class SalesmanForm(ModelForm):
    class Meta:
        model = Salesmen
        exclude = ('id',)

class SaleForm(ModelForm):
    class Meta:
        model = Sales
        exclude = ('id',)