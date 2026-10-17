from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model= JobApplication
        fields= ['company', 'job_title', 'status', 'applied_date']

    applied_date = forms.DateField(
                        widget=forms.DateInput(attrs={
                            'type': 'date',
                            'class': 'form-control'
                        })
                    )