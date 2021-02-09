from django.shortcuts import render
from django.http import HttpResponse
from .models import City
from .forms import CityForm
import requests


# Create your views here.


def index(request):
    if request.method == "POST":
        form = CityForm(request.POST or None)
        if form.is_valid():
            city_name = form.cleaned_data["city"]
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=277607675933f3fb5143251f8a1c85ee&units=metric"
            res = requests.get(url)
            data = res.json()

            city_weather = {
                "city": city_name,
                "description": data["weather"][0]["description"],
                "temprature": data["main"]["temp"],
                "wind": data["wind"]["speed"],
                "icon": data["weather"][0]["icon"],
            }
            context = {"weather": city_weather, "form": form}
        return render(request, "weather/city.html", context)
    else:
        form = CityForm()
        return render(request, "weather/index.html", {"form": form})

