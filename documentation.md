# Agric Advisor Global - Technical Documentation

## 1. System Overview
**Agric Advisor Global** is an advanced multi-agent AI platform designed for high-fidelity agronomic consulting on a global scale. Built for a premium hackathon experience, it provides localized advice to farmers in **Europe, North America, and West Africa**. The system integrates real-time climate signatures, global commodity market indices, and multi-lingual vocal guidance.

## 2. Architecture
The system follows a polished **Multi-Agent Architecture**:
*   **Web Dashboard (Flask)**: A high-end interface implementing **Glassmorphism** for a professional, technical aesthetic.
*   **Data Agent**: The "Discovery" layer. It aggregates environmental data from OpenWeather and economic indices from global market scrapers.
*   **Knowledge Agent**: The "Intelligence" layer. It synthesizes complex datasets into actionable strategic wisdom via Google Gemini AI.
*   **Report Agent**: The "Communication" layer. It dispatches localized alerts and voice-links to users globally.

## 3. Technology Stack
*   **Language**: Python 3.9+
*   **Web Framework**: Flask
*   **AI/LLM**: Google Gemini (`gemini-flash-latest`)
*   **Voice/TTS**: Google Translate TTS (`gTTS`) - selected for 100+ language support.
*   **Design System**: Vanilla CSS3 with **Glassmorphism** and the **Outfit** typography.
*   **External APIs**:
    *   **Weather**: OpenWeatherMap API (Global support)
    *   **Market Data**: Selina Wamucii Global Insight Scraper (covering UK, USA, FR, DE, CA, NG).
    *   **SMS**: Twilio API (Global reach)

## 4. Component Details

### 4.1. Services Layer (`/services`)
*   **`WeatherService`**: Standardized global weather fetching with resilient error handling.
*   **`MarketService`**: Dynamically detects the user's region (e.g., London, New York) and provides price indices in local currencies (£, $, €, ₦).
*   **`LLMService`**: Strategic prompt engineering for cross-continental crop advice.
*   **`TTSService`**: High-quality vocalization in English, Spanish, French, German, Italian, Portuguese, and West African languages.

### 4.2. Agents Layer (`/agents`)
*   **`DataAgent`**: Centralizes the multi-service data stream into a single context object.
*   **`KnowledgeAgent`**: Directs Gemini to provide short, actionable insights suitable for SMS/Voice.
*   **`ReportAgent`**: Manages international phone numbers and localized messaging.

### 4.3. Application Layer (`app.py`)
*   **Networking**: Configured to listen on `0.0.0.0` for maximum accessibility across local networks.
*   **Normalization**: Smart detection of country codes for phone number delivery.

## 5. Global Data Flow Example
1.  **Input**: User in **London** requests advice for **Corn** in **Spanish**.
2.  **Market Logic**: `MarketService` identifies the UK region, fetches the GBP price index.
3.  **Synthesis**: Gemini generates advice focused on the UK climate, translated into Spanish.
4.  **Vocalization**: `TTSService` generates a Spanish MP3.
5.  **Output**: Dashboard displays Glassmorphic cards with "Corn £1.20/kg" and a Spanish audio player.

## 6. Setup & Configuration
Requirement: A `.env` file with global API keys for OpenWeather, Gemini, and Twilio.

To start the global server:
```bash
python app.py
```

## 7. UI Access
*   **Local**: [http://127.0.0.1:5000](http://127.0.0.1:5000)
*   **Network**: [http://<your-ip>:5000](http://<your-ip>:5000)
