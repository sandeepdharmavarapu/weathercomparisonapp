from django.shortcuts import render
import requests
import json
from .forms import WeatherForm

# Create your views here.
def weather(request):
	if request.method == "POST":
		form = WeatherForm(request.POST)
		API_KEY = 'd0c1d043aabb438a8699081aaf0535c8'
		if form.is_valid():
			loc1=form.cleaned_data['loc1']
			print(loc1)
			loc2=form.cleaned_data['loc2']
			result1 = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}".format(loc1,API_KEY))
			result2 = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}".format(loc2,API_KEY))
			t = result1.content.decode('utf-8')
			t1 = result2.content.decode('utf-8')
			result1 =json.loads(t)
			result2=json.loads(t1)
			form=WeatherForm()
			return render(request,'result.html',{"form":form, "result1":result1, "result2":result2})
	else:		
		form=WeatherForm()
	return render(request,'weather.html',{"form":form})
	



