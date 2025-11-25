from django import forms
from . import models
class PAYEAgentForm(forms.ModelForm):
    agent_password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    class Meta:
        model = models.PAYEAgent
        fields = ['payer_id', 'agent_name', 'agent_rc_num', 'contact_email', 'contact_phone', 'address', 'agent_password']
        widgets = {
            'agent_password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("agent_password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if password != confirm_password:
            raise forms.ValidationError("Password and Confirm Password do not match.")
        return cleaned_data