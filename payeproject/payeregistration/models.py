from django.db import models
from django.contrib.auth.hashers import check_password
# Create your models here.
class PAYEAgent(models.Model):
    payer_id = models.CharField(max_length=100, primary_key=True)
    agent_name = models.CharField(max_length=255, unique=True)
    agent_rc_num = models.CharField(max_length=50, unique=True)
    contact_email = models.EmailField(unique=True)
    contact_phone = models.CharField(max_length=20)
    address = models.TextField()
    agent_password = models.CharField(max_length=128)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agent_name

    def check_password(self, raw_password):
        return check_password(raw_password, self.agent_password)
    