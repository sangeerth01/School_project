from django import forms 
from . models import Add

class addForm(forms.ModelForm):
   class Meta:
      model = Add
      fields = ['name','age','email']