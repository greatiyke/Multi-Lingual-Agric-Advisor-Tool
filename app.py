from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from agents.data_agent import DataAgent
from agents.knowledge_agent import KnowledgeAgent
from agents.report_agent import ReportAgent
from services.tts_service import TTSService

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_advice', methods=['POST'])
def get_advice():
    try:
        location = request.form.get('location')
        crop = request.form.get('crop')
        language = request.form.get('language')
        phone = request.form.get('phone')

        if not location or not crop:
            return jsonify({"error": "Location and Crop are required"}), 400

        # 1. Data Agent
        data_agent = DataAgent()
        data = data_agent.gather_data(location, crop)
        
        # 2. Knowledge Agent
        knowledge_agent = KnowledgeAgent()
        advice = knowledge_agent.process_advice(data, language)

        # Generate Audio
        tts_service = TTSService()
        audio_filename = tts_service.generate_audio(advice, language)
        audio_url = f"{request.host_url}static/audio/{audio_filename}" if audio_filename else None
        
        # 3. Report Agent (Optional)
        sms_status = None
        if phone:
            # Basic normalization for Nigeria
            if phone.startswith("0") and len(phone) == 11:
                phone = "+234" + phone[1:]
            
            report_agent = ReportAgent()
            # Append audio link to SMS if available
            sms_message = advice
            if audio_url:
                sms_message += f"\n\nListen here: {audio_url}"
                
            result = report_agent.send_report(phone, sms_message)
            sms_status = result.get("status")

            if result.get("status") == "failed":
                sms_status = f"Failed: {result.get('error')}"

        return jsonify({
            "advice": advice,
            "sms_status": sms_status,
            "data": data,
            "audio_file": audio_filename
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
