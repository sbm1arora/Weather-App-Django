from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import City
from .forms import CityForm
import requests


# Create your views here.


def show_weather(request):
    weather_data = []
    cities = City.objects.all()
    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city.name}&appid=277607675933f3fb5143251f8a1c85ee&units=metric"
        res = requests.get(url)
        data = res.json()

        city_weather = {
            "city": city.name,
            "description": data["weather"][0]["description"],
            "temprature": data["main"]["temp"],
            "wind": data["wind"]["speed"],
            "icon": data["weather"][0]["icon"],
        }
        weather_data.append(city_weather)
    context = {"weather": weather_data}

    return render(request, "weather/city.html", context)


def index(request):
    if request.method == "POST":
        form = CityForm(request.POST or None)
        if form.is_valid():
            form = CityForm()
        return redirect("show_weather")
    else:
        form = CityForm()

    return render(request, "weather/index.html", {"form": form})

