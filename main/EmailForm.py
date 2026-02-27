
from django import forms

BRANCH_CHOICES = [
    ('CSE', 'CSE'),
    ('IT', 'IT'),
    ('ECE', 'ECE'),
    ('EEE', 'EEE'),
    ('CIVIL', 'CIVIL'),
    ('MECH', 'MECH'),
]

class EmailForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100)
    branch = forms.ChoiceField(choices=BRANCH_CHOICES)   
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)