from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from payeregistration.models import PAYEAgent

class Staff(models.Model):
    employee_pid = models.CharField(max_length=20, primary_key=True)
    employee_name = models.CharField(max_length=100)
    employer_id = models.ForeignKey(PAYEAgent, on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone_number = PhoneNumberField(null=True)


class PayeComputation(models.Model):
    computation_id = models.CharField(max_length=20, primary_key=True)
    employee_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    employer_id = models.ForeignKey(PAYEAgent, on_delete=models.CASCADE, null=True)
    gross_income = models.DecimalField(max_digits=10, decimal_places=2)
    paye_amount = models.DecimalField(max_digits=10, decimal_places=2)
    computation_date = models.DateField(auto_now_add=True)
    tax_year = models.CharField(max_length=9)  # e.g., "2023-2024"



