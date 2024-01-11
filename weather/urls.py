from django.urls import path
from weather.views import WeatherAPIView

urlpatterns = [
    path('weather/', WeatherAPIView.as_view()),
]
