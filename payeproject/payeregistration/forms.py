from django import forms
from . import models
class PAYEAgentForm(forms.ModelForm):
    agent_password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    class Meta:
        model = models.PAYEAgent
        fields = ['payer_id', 'agent_name', 'agent_rc_num', 'contact_email', 'contact_phone', 'address', 'agent_password']

    def clean_payer_id(self):
        payer_id = self.cleaned_data.get('payer_id')
        if models.PAYEAgent.objects.filter(payer_id=payer_id).exists():
            raise forms.ValidationError("Payer ID already exists.")
        return payer_id
    def clean_agent_password(self):
        password = self.cleaned_data.get('agent_password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return password
    
    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        if len(confirm_password) < 8:
            raise forms.ValidationError("Confirm Password must be at least 8 characters long.")
        return confirm_password
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("agent_password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
        return cleaned_data