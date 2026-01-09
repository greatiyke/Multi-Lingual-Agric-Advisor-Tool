from services.llm_service import LLMService

class KnowledgeAgent:
    def __init__(self):
        self.llm_service = LLMService()

    def process_advice(self, data, language):
        weather_data = data.get("weather")
        market_data = data.get("market")
        
        advice = self.llm_service.generate_advice(weather_data, market_data, language)
        return advice
