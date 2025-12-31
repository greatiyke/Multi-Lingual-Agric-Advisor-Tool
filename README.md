# 🌱 Agric Advisor AI

**Empowering Farmers, One SMS at a Time.**

Agric Advisor AI is a localized, multi-agent system designed to provide personalized agronomic advice to rural farmers in Nigeria. By bridging the gap between complex data and accessible technology, it delivers real-time, actionable insights via **Web, SMS, and Voice** in local indigenous languages.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![Twilio](https://img.shields.io/badge/Twilio-SMS-red)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange)

## 🚀 Features

*   **🌍 Multi-Lingual Support**: Generates advice in **English, Yoruba, Hausa, Igbo, and Pidgin**.
*   **🤖 Multi-Agent Architecture**:
    *   **Data Agent**: Fetches real-time weather (OpenWeatherMap) and market prices (Web Scraper).
    *   **Knowledge Agent**: Uses **Google Gemini** to synthesize data into expert agronomic advice.
    *   **Report Agent**: Delivers advice via SMS.
*   **🗣️ Voice Feature**: text-to-Speech (TTS) integration for illiterate farmers.
*   **📱 SMS Integration**: Sends advice directly to feature phones using Twilio.
*   **🇳🇬 Localized**: automatically formats Nigerian phone numbers and scrapes local market exchanges.

## 🛠️ Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/agric-advisor.git
    cd agric-advisor
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Setup**:
    Create a `.env` file in the root directory and add your API keys:
    ```env
    OPENWEATHER_API_KEY=your_key_here
    GEMINI_API_KEY=your_key_here
    TWILIO_ACCOUNT_SID=your_sid_here
    TWILIO_AUTH_TOKEN=your_token_here
    TWILIO_FROM_NUMBER=your_twilio_number
    ```

## 🏃‍♂️ Usage

1.  **Run the Application**:
    ```bash
    python app.py
    ```

2.  **Access the Web Interface**:
    Open your browser and navigate to `http://127.0.0.1:5000`.

3.  **Get Advice**:
    *   Enter your Location (e.g., "Lagos").
    *   Enter your Crop (e.g., "Maize").
    *   Select your Language.
    *   (Optional) Enter your phone number for SMS.
    *   Click **Get Advice** to see and hear the recommendation!

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
