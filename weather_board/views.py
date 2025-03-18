from flask import Blueprint, render_template, url_for
from .weather_manager import get_weather, graph_weather

views = Blueprint("views", __name__)

@views.route('/')
def home():
    weather = get_weather()
    if weather:
        graph_weather(weather)
        return render_template('home.html', weather=weather)
    else:
        # TODO: Create error page if api response fails
        return '<p>Sorry, there was an error retrieving the weather information.</p>'