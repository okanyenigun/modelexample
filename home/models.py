from django.db import models

class SalesmanManager(models.Manager):
    def create_salesman(self, data):
        salesman = self.create(first_name=data["first_name"],last_name=data["last_name"],age=data["age"],place=data["place"])
        return salesman


class Salesmen(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    first_name = models.CharField(db_column='FIRST_NAME', max_length=255, blank=True, null=True) 
    last_name = models.CharField(db_column='LAST_NAME', max_length=255, blank=True, null=True) 
    age = models.IntegerField(db_column='AGE', blank=True, null=True) 
    place = models.CharField(db_column='PLACE', max_length=255, blank=True, null=True) 

    objects = SalesmanManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        managed = False
        db_table = 'SALESMEN'


class SalesManager(models.Manager):
    def create_sales(self, data):
        sale = self.create(salesman=data["salesman"], quantity=data["quantity"],unit_price=data["unit_price"])
        return sale

class Sales(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    salesman = models.ForeignKey('Salesmen', models.DO_NOTHING, db_column='SALESMAN_ID', blank=True, null=True) 
    quantity = models.IntegerField(db_column='QUANTITY', blank=True, null=True) 
    unit_price = models.FloatField(db_column='UNIT_PRICE', blank=True, null=True) 

    objects = SalesManager()

    def __str__(self):
        return f"{self.salesman} : {self.quantity}"

    class Meta:
        managed = False
        db_table = 'SALES'


