import os
import google.generativeai as genai

class LLMService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("OPENAI_API_KEY") # Fallback if user put it in OPENAI_API_KEY
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-flash-latest')
        else:
            self.model = None

    def generate_advice(self, weather_data, market_data, language):
        print(f"[LLMService] Generating real advice in {language} using Gemini...")
        
        if not self.model:
            print("[LLMService] Error: GEMINI_API_KEY not found.")
            return "Error: API key missing."

        try:
            prompt = (
                f"You are an expert agricultural advisor. Provide short, actionable agronomic advice for a farmer in {market_data.get('location')} "
                f"growing {market_data.get('crop')}. "
                f"Current weather: {weather_data.get('condition')}, {weather_data.get('temperature')}°C. "
                f"Market status: Price is {market_data.get('current_price')}. "
                f"Please provide the advice in the {language} language. Keep it under 160 characters if possible for SMS."
            )

            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"[LLMService] Error generating advice: {e}")
            return "Error generating advice. Please try again."
