import requests
from django.shortcuts import render
import os
def index(request):
    return render(request, 'wea_app/base.html')

def get_weather(request):
    city = request.GET.get('city', 'Bangkok') 
    api_key = os.getenv('OPENWEATHER_API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    
    context = {}
    try:
        response = requests.get(url).json()
        
        if response.get('cod') == 200:
            weather_main = response['weather'][0]['main']
            temp = response['main']['temp']
            
            # Logic เลือก Theme สีตามสภาพอากาศ
            bg_class = 'from-blue-400 to-blue-600' # Default (Clear)
            if 'Rain' in weather_main:
                bg_class = 'from-gray-700 to-slate-900' # ฝนตก (มืดๆ)
            elif 'Clouds' in weather_main:
                bg_class = 'from-indigo-400 to-cyan-400' # เมฆมาก
            elif temp > 35:
                bg_class = 'from-orange-500 to-red-600' # ร้อนจัด
            elif temp < 20:
                # อากาศเย็น: ม่วง -> ชมพู (Morning vibe)
                bg_class = 'from-purple-500 to-pink-500'
            
            context = {
                'city': response['name'],
                'temp': int(temp),
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                'bg_class': bg_class,
                'found': True
            }
        else:
            context = {'found': False}
            
    except Exception as e:
        context = {'found': False}

    return render(request, 'wea_app/partials/weather_card.html', context)