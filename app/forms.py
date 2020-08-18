 
from django import forms
from .models import 

      
class ProjectRatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['project', 'pub_date', 'user']