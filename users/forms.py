# users/forms.py
from django import forms
from .models import MemberProfile

class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = ['full_name', 'date_of_birth', 'age', 'gender', 'phone_number', 'bank_account_number', 'bank_name']
