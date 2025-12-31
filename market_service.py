import requests
from bs4 import BeautifulSoup
import re

class MarketService:
    def __init__(self):
        self.base_url = "https://www.selinawamucii.com/insights/prices/nigeria"

    def get_market_prices(self, crop, location):
        print(f"[MarketService] Fetching real prices for {crop} in Nigeria (via Selina Wamucii)...")
        
        try:
            # Construct URL (simple slugification)
            crop_slug = crop.lower().replace(" ", "-")
            url = f"{self.base_url}/{crop_slug}/"
            
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Look for the price text
                # Pattern: "approximate wholesale price range ... is between US$ X and US$ Y"
                text_content = soup.get_text()
                price_match = re.search(r"wholesale price range.*?between US\$ ([\d\.]+) and US\$ ([\d\.]+)", text_content, re.IGNORECASE)
                
                if price_match:
                    low_price = float(price_match.group(1))
                    high_price = float(price_match.group(2))
                    avg_price_usd = (low_price + high_price) / 2
                    
                    # Convert to Naira (Approximate rate, e.g., 1 USD = 1500 NGN)
                    exchange_rate = 1500
                    price_ngn = avg_price_usd * exchange_rate
                    
                    return {
                        "crop": crop,
                        "location": "Nigeria (National Average)",
                        "current_price": f"₦{price_ngn:,.2f} / kg",
                        "trend": "Live Data",
                        "market_demand": "High (Inferred)"
                    }
                else:
                    print("[MarketService] Price pattern not found in page.")
            else:
                print(f"[MarketService] Failed to fetch page: {response.status_code}")
                
        except Exception as e:
            print(f"[MarketService] Error scraping data: {e}")

        # Fallback to mock if scraping fails
        print("[MarketService] Fallback to mock data.")
        return {
            "crop": crop,
            "location": location,
            "current_price": "₦500.00 (Mock)",
            "trend": "Stable",
            "market_demand": "Medium"
        }
