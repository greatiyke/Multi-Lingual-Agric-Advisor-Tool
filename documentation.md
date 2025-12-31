# Agric Advisor AI - Technical Documentation

## 1. System Overview
**Agric Advisor AI** is a multi-agent system designed to provide personalized agronomic advice to farmers in Nigeria. It leverages real-time data and Large Language Models (LLMs) to generate actionable insights in local languages and delivers them via **SMS** and **Voice** (Text-to-Speech).

## 2. Architecture
The system follows a **Multi-Agent Architecture** where specialized agents handle distinct responsibilities:

*   **Data Agent**: Responsible for gathering raw context. It interfaces with external APIs to fetch weather and market data.
*   **Knowledge Agent**: The "brain" of the system. It synthesizes the raw data into agronomic advice and translates it using Generative AI.
*   **Report Agent**: The delivery mechanism. It formats the advice and sends it to the user via SMS, including a link to the audio advice.
*   **Orchestrator (Flask App)**: The central controller that receives user input, coordinates the agents in sequence, generates audio, and presents the results via a Web UI.

## 3. Technology Stack
*   **Language**: Python 3.9+
*   **Web Framework**: Flask
*   **AI/LLM**: Google Gemini (`gemini-flash-latest`)
*   **Voice/TTS**: Google Text-to-Speech (`gTTS`)
*   **External APIs**:
    *   **Weather**: OpenWeatherMap API
    *   **Market Data**: Web Scraping (`BeautifulSoup`) of *Selina Wamucii* market data.
    *   **SMS**: Twilio API
*   **Frontend**: HTML5, Bootstrap 5

## 4. Component Details

### 4.1. Services Layer (`/services`)
This layer handles direct interactions with external tools.
*   **`WeatherService`**: Connects to OpenWeatherMap to get temperature, humidity, and conditions.
*   **`MarketService`**: Scrapes live crop prices from online sources. Includes fallback to mock data.
*   **`LLMService`**: Interaction with Google Gemini API to generate and translate advice.
*   **`MessagingService`**: Wraps the Twilio Client to send SMS messages.
*   **`TTSService`**: [NEW] uses `gTTS` to convert the generated advice text into an MP3 audio file saved in `static/audio`.

### 4.2. Agents Layer (`/agents`)
This layer abstracts the business logic.
*   **`DataAgent`**: Aggregates data from both `WeatherService` and `MarketService`.
*   **`KnowledgeAgent`**: Uses `LLMService` to process the context and generate advice.
*   **`ReportAgent`**: Uses `MessagingService` to deliver the output. It now appends an audio link to the SMS body.

### 4.3. Application Layer (`app.py`)
*   **Phone Number Normalization**: Automatically converts local Nigerian numbers (e.g., `070...`) to international format (`+234...`) before sending to Twilio.
*   **Audio Integration**: Calls `TTSService` after advice generation and passes the audio URL to the frontend and Report Agent.

## 5. Data Flow
1.  **User Input**: Location: "Lagos", Crop: "Maize", Language: "Yoruba".
2.  **Context**: System fetches "Rainy, 28°C" (Weather) and "₦650/kg" (Market).
3.  **Advice Generation**: Gemini returns translated advice: *"E gbin agbado ni kiakia..."*.
4.  **Audio Generation**: `TTSService` converts the Yoruba text to an MP3 file.
5.  **Delivery**: 
    *   **Web**: Displays text and an HTML5 Audio Player.
    *   **SMS**: Sends text + "Listen here: http://.../audio.mp3".

## 6. Deployment
To publish this app (e.g., to Google Play Store), it must first be hosted on a public server.
*   **Deployment Guide**: See `deployment_guide.md` for full instructions on hosting and converting to an Android App Bundle (.aab).

## 7. Setup & Configuration
The system requires a `.env` file with the following keys:
*   `OPENWEATHER_API_KEY`
*   `GEMINI_API_KEY`
*   `TWILIO_ACCOUNT_SID`
*   `TWILIO_AUTH_TOKEN`
*   `TWILIO_FROM_NUMBER`

To run the application:
```bash
python app.py
```

## 8. Accessing the Application
*   **Standard URL**: [http://127.0.0.1:5000](http://127.0.0.1:5000)
*   **Custom URL** (if configured via `setup_domain.bat`): [http://Agric_Advisor:5000](http://Agric_Advisor:5000)
