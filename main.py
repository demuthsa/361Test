import argparse
import pyfiglet
from simple_chalk import chalk
import requests

# API Key (Openweathermap)
API_KEY = "e535cd25e68edb4ec4416a8e6c552856"

# API URL for Openweather
API_URL = "https://api.openweathermap.org/data/2.5/weather"

# Weather codes to weather icons
WEATHER_ICONS = {
    # day icons
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "⛈",
    "13d": "🌨",
    "50d": "🌫",
    # night icons
    "01n": "🌙",
    "02n": "☁️",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "⛈",
    "13n": "🌨",
    "50n": "🌫",
}


# Welcome 
print(pyfiglet.figlet_format("Weather App"))
print(chalk.green(
    "Welcome to the Weather App! Get real-time weather information for any city or country.\n"
    "Try the --units option to see temperatures in Celsius or Fahrenheit!\n"
    "Type --help to see all options.\n"
))
print(chalk.yellow(
    "Tip: You can press the up arrow key to cycle through your previous commands and repeat or modify them as needed."
))

# API URL with query parameters
parser = argparse.ArgumentParser(
    description="Check the weather for a certain specific location",
    epilog="Example usage: python main.py London or python main.py --units metric"
)

parser.add_argument(
    "location", 
    help="Specify the city or country to get the current weather information."
         "Seeing the weather for your location can help you plan your day."
)

parser.add_argument(
    '--units', 
    choices=['imperial', 'metric', 'standard'], 
    default='imperial', 
    help="Set the units for temperature (imperial, metric, standard). Default is 'imperial"
         "Choose 'metric' for Celsius or 'imperial' for Fahrenheit."
         "This allows for personalized temperature display."
)
# Heuristic 3 - Lets user gather more info
parser.add_argument(
    '--additional', 
    action='store_true', 
    help="Display additional weather information such as Wind Speed, Humidity & Pressure."
)



args = parser.parse_args()
url = f"{API_URL}?q={args.location}&appid={API_KEY}&units={args.units}"

# Make API request and parse response using requests module
response = requests.get(url)
if response.status_code != 200:
    print(chalk.red("Error: Unable to retrieve weather information"))
    exit()

# Parse the JSON response from the API and extract the weather information
data = response.json()

# Get information from the response
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]
# Determine the unit symbol based on the 'units' argument
unit_symbol = "°F" if args.units == 'imperial' else "°C" if args.units == 'metric' else "K"

if args.additional:
    wind_speed = data["wind"]["speed"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

# Output with weather icons
weather_icon = WEATHER_ICONS.get(icon, "")
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += f"{weather_icon} {description}\n"
output += f"Temperature: {temperature} {unit_symbol}\n"
output += f"Feels like: {feels_like} {unit_symbol}\n"
# Additional info
if args.additional:
    output += f"Wind Speed: {wind_speed} mph\n"
    output += f"Humidity: {humidity}%\n"
    output += f"Pressure: {pressure} hPa\n"

# Print Output
print(chalk.green(output))
print(chalk.yellow(
    "Reminder: This service uses a third-party weather API with rate limits."
    "Excessive requests may lead to temporary unavailability."
))

