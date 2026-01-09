import requests
import time

def test_yoruba_voice():
    url = "http://127.0.0.1:5000/get_advice"
    data = {
        "location": "Lagos",
        "crop": "Maize",
        "language": "Yoruba"
    }
    
    print("Sending Yoruba request to Web App...")
    start = time.time()
    try:
        response = requests.post(url, data=data)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            json_data = response.json()
            print("Response JSON keys:", json_data.keys())
            audio_file = json_data.get("audio_file")
            
            if audio_file:
                print(f"Audio File Returned: {audio_file}")
                # Try fetching the audio file
                audio_url = f"http://127.0.0.1:5000/static/audio/{audio_file}"
                audio_resp = requests.get(audio_url)
                if audio_resp.status_code == 200:
                    print(f"Audio file downloadable. Size: {len(audio_resp.content)} bytes")
                else:
                    print(f"Error downloading audio file: {audio_resp.status_code}")
            else:
                print("No 'audio_file' in response!")
                print("Full Response:", json_data)
        else:
            print("Request failed:", response.text)
            
    except Exception as e:
        print(f"Exception: {e}")
    
    print(f"Duration: {time.time() - start:.2f}s")

if __name__ == "__main__":
    test_yoruba_voice()
