from django.forms import FloatField
from django.shortcuts import render, redirect
from django.views import View
from .forms import SalesmanForm, SaleForm
from .models import Sales, Salesmen

from django.db.models import F

class MainView(View):

    def get(self,request):
        form_salesman = SalesmanForm()
        form_sale = SaleForm()
        value = Sales.objects.filter(salesman=2).select_related('salesman')
        print(value)
        print(value.query)
        return render(request, './templates/index.html',{'formSalesman': form_salesman, 'formSale':form_sale})

    def post(self,request):
        if "send_salesman" in request.POST:
            form = SalesmanForm(request.POST)
            if form.is_valid():
                new_record = form.save()
                print(new_record)
        elif "send_sales" in request.POST:
            form = SaleForm(request.POST)
            if form.is_valid():
                new_record = form.save()
                print(new_record)
        return redirect('main')