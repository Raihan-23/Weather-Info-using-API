import requests

API_KEY = '49d05ec6dfd6a066eba407c6003c577d'
city = 'New York'
weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

response = requests.get(weather_url)

if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.status_code)
