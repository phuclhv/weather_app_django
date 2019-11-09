import requests
from django.shortcuts import render
from .models import City
# Create your views here.
def index(request):
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=b843deeef7e0bc94223e723366ed9d94'
  city = 'Seattle '

  weather_data = []
  cities = City.objects.all()

  for city in cities:
    r = requests.get(url.format(city)).json()
    city_weather = {
      'city' : city.name,
      'temperature': r['main']['temp'],
      'description': r['weather'][0]['description'],
      'icon': r['weather'][0]['icon'],
    }
    weather_data.append(city_weather)
  print(weather_data)
  context = {'weather_data': weather_data
  }
  return render(request, 'weather/weather.html', context )