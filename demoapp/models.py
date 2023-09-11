from django.db import models

class Employee(models.Model):
    emp_id=models.PositiveIntegerField(primary_key=True)
    emp_name=models.CharField(max_length=100,blank=False)
    emp_gender=models.CharField(max_length=10,blank=False)
    emp_dob=models.DateField(blank=False)
    emp_dept=models.CharField(max_length=100,blank=False)
    emp_email=models.EmailField(max_length=100,blank=False,unique=True)
    emp_contactno=models.BigIntegerField(blank=False,unique=True)

    class Meta:
        db_table="employee_table"

class Registration(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100,blank=False)
    gender_choices=( ("M","Male") , ("F","Female") , ("Others","Prefer not to say") )
    gender=models.CharField(blank=False,choices=gender_choices,max_length=10)
    dateofbirth=models.CharField(blank=False,max_length=20)
    email=models.EmailField(max_length=100,blank=False,unique=True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    password = models.CharField(max_length=100, blank=False)
    contact = models.BigIntegerField(blank=False, unique=True)
    location = models.CharField(max_length=100, blank=False)
    registrationtime=models.DateTimeField(blank=False,auto_now=True)

    class Meta:
        db_table = "registration_table"

class Department(models.Model):
    dept_id = models.PositiveIntegerField(primary_key=True)
    dept_name = models.CharField(max_length=50,blank=False)
    dept_hod = models.CharField(max_length=50,blank=False)
    location_choices=(  ("C-Block","Computer Block") , ("M-Block","Mechanical Block") , ("R&D Block","R&D Block")   )
    dept_location = models.CharField(max_length=50,blank=False,choices=location_choices)

    class Meta:
        db_table = "department_table"