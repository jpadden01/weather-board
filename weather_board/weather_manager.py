import requests, json
from matplotlib import pyplot as plt

url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 49.2497,
	"longitude": -123.1193,
	"daily": ["precipitation_probability_max", "temperature_2m_max", "temperature_2m_min", "precipitation_sum", "sunrise", "sunset"],
	"hourly": "temperature_2m",
	"current": ["temperature_2m", "wind_speed_10m", "wind_direction_10m", "apparent_temperature"],
	"timezone": "America/Los_Angeles",
	"forecast_days": 1
}

def get_weather():
    r = requests.get(url, params=params)
    data = json.loads(r.content)
    return data

def graph_weather(weather):
    temps = weather['hourly']['temperature_2m']
    plt.plot(temps)
    plt.savefig('weather_board/static/temps.png')

'''
Weather keys:

-current
  -time
  -temperature_2m
  -wind_speed_10m
  -wind_direction_10m
  -apparent_temperature
-hourly
  -temperature_2m
-daily
  -precipitation_probability_max
  -temperature_2m_max
  -temperature_2m_min
  -precipitation_sum
  -sunrise
  -sunset
'''

if __name__ == '__main__':
    # For testing
    weather = get_weather()
    print(json.dumps(weather, indent=2))
    graph_weather(weather)