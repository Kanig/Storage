from django import forms
from .models import landing

class LandingForm(forms.ModelForm):

	class Meta:
		model = landing
		exclude = [""]