import logging
import urllib
import json

from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from rest_framework import status

from digital_oracle_test.settings import openweather_api

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()

logger.addHandler(console_handler)


class WeatherAPIView(APIView):

    def get(self, request):
        city = request.GET.get('city')
        logger.info(f'Received city from request: {city}')

        if not city:
            return Response({'error': 'City not provided'}, status=status.HTTP_400_BAD_REQUEST)

        cached_data = cache.get(city)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)

        try:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={openweather_api}'
            source = urllib.request.urlopen(url).read()

            logger.info(f"Requested weather data from {url}")

            list_of_data = json.loads(source)

            data = {
                'city': city,
                'temperature': f'{list_of_data["main"]["temp"]} °C',
                'pressure': f'{list_of_data["main"]["pressure"]} hPa',
                'wind': f'{list_of_data["wind"]["speed"]} meter/sec'
            }
            cache.set(city, data, 1800)
            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {'error': f'Error getting weather data: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
