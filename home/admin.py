from django.contrib import admin
from .models import Sales, Salesmen

admin.site.register(Salesmen)
admin.site.register(Sales)