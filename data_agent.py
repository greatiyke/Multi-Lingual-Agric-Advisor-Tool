from services.weather_service import WeatherService
from services.market_service import MarketService

class DataAgent:
    def __init__(self):
        self.weather_service = WeatherService()
        self.market_service = MarketService()

    def gather_data(self, location, crop):
        weather_data = self.weather_service.get_weather(location)
        market_data = self.market_service.get_market_prices(crop, location)
        return {
            "weather": weather_data,
            "market": market_data
        }
