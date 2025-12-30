# bot.py - Daily Summary Robot (Phase 1: Get the weather)
import requests
import config  # Import our own configuration file

def get_weather():
    "Get weather data for a specified city from OpenWeatherMap"
    
    # Read configuration from config.py
    api_key = config.OPENWEATHER_API_KEY
    city = config.CITY

    # Build API request URL (using standard city weather API)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        # Send GET request
        response = requests.get(url)
        
        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            data = response.json()
            
            # Extract the information we need from the returned JSON data
            main = data['main']
            weather_info = data['weather'][0]
            
            temperature = main['temp']
            humidity = main['humidity']
            description = weather_info['description']
            
            # Format the weather report
            weather_report = f"""
========== Weather Report ==========
City: {city}
Condition: {description}
Temperature: {temperature}°C
Humidity: {humidity}%
============================
"""
            return weather_report
            
        else:
            # Handle unsuccessful API response
            return f"Error: Weather data cannot be obtained. The API returns a status code: {response.status_code}\nPlease check the city name and API key."
            
    except Exception as e:
        # Handle network errors or other exceptions
        return f"Program error: {str(e)}"
# Main program entry point
if __name__ == "__main__":
    print("Daily Summary: Robot starts up...")
    print("I'm getting weather information...")
    
    weather = get_weather()
    print(weather)
    
    print("Today's weather information has been retrieved!")