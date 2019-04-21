from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.emp_name

class Workhour(models.Model):
    emp_name=models.ForeignKey('Employee',on_delete=models.PROTECT)
    days=models.DateField()


    def __int__(self):
        return self.days

class Salary(models.Model):
    days=models.ForeignKey('Workhour',on_delete=models.PROTECT)
    credited_salary= models.IntegerField()
    salary_date= models.DateField()


class Login(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)

