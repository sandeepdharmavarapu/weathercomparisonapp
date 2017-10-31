from django import forms
from .models import Weather
# Create your forms here.

class WeatherForm(forms.ModelForm):

	class Meta:
		model = Weather
		fields = ('loc1','loc2')


