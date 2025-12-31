import requests

def test_app():
    url = "http://127.0.0.1:5000/get_advice"
    payload = {
        "location": "Lagos",
        "crop": "Maize",
        "language": "English",
        "phone": "" # Optional
    }
    
    print(f"Sending request to {url}...")
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            data = response.json()
            print("\n--- Success! ---")
            print(f"Advice: {data.get('advice')}")
            print(f"Weather: {data.get('data', {}).get('weather', {}).get('condition')}")
            print(f"Market Price: {data.get('data', {}).get('market', {}).get('current_price')}")
        else:
            print(f"Failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Is the Flask app running?")

if __name__ == "__main__":
    test_app()
