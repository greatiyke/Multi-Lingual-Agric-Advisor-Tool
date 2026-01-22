import requests

def test_global_advice():
    payload = {
        "location": "New York",
        "crop": "Wheat",
        "language": "English",
        "phone": ""
    }
    
    print(f"Testing global advice for: {payload['location']}...")
    try:
        response = requests.post("http://127.0.0.1:5000/get_advice", data=payload)
        print(f"Status: {response.status_code}")
        data = response.json()
        
        if "error" in data:
            print(f"Error: {data['error']}")
        else:
            print("\n--- RESULTS ---")
            print(f"Advice: {data['advice'][:100]}...")
            print(f"Market: {data['data']['market']['current_price']} ({data['data']['market']['location']})")
            print(f"Weather: {data['data']['weather']['temperature']}°C")
            print(f"Audio File: {data['audio_file']}")
            
            if data['audio_file']:
                print("Audio generated successfully.")
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    test_global_advice()
