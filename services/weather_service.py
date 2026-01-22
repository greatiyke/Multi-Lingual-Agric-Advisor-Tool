import requests
import os

class WeatherService:
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, location):
        print(f"[WeatherService] Fetching real weather for {location}...")
        if not self.api_key:
            print("[WeatherService] Error: OPENWEATHER_API_KEY not found.")
            return {"error": "API key missing"}

        try:
            params = {
                "q": location,
                "appid": self.api_key,
                "units": "metric"
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            return {
                "location": data.get("name"),
                "temperature": data["main"]["temp"],
                "condition": data["weather"][0]["description"].capitalize(),
                "humidity": data["main"]["humidity"],
                "forecast": "Check local forecast for details." # Current weather API doesn't give forecast without another call
            }
        except Exception as e:
            print(f"[WeatherService] Error fetching weather for {location}: {e}")
            return {
                "location": location,
                "temperature": "N/A",
                "condition": "unavailable",
                "humidity": "N/A",
                "forecast": "Service temporarily unavailable."
            }
