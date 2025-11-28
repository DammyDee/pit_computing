from django.db import models

class PayeComputation(models.Model):
    employee_id = models.CharField(max_length=20)
    employee_name = models.CharField(max_length=100)
    gross_income = models.DecimalField(max_digits=10, decimal_places=2)
    paye_amount = models.DecimalField(max_digits=10, decimal_places=2)
    computation_date = models.DateField(auto_now_add=True)
    tax_year = models.CharField(max_length=9)  # e.g., "2023-2024"

    