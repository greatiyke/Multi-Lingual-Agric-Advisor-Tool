import os
from dotenv import load_dotenv
from agents.data_agent import DataAgent
from agents.knowledge_agent import KnowledgeAgent
from agents.report_agent import ReportAgent

# Load environment variables
load_dotenv()

def main():
    print("=== Agricultural Advisor Multi-Agent System ===")
    
    # Inputs (In a real app, these could come from an API request or CLI args)
    location = input("Enter location (e.g., Lagos): ") or "Lagos"
    crop = input("Enter crop (e.g., Maize): ") or "Maize"
    language = input("Enter preferred language (e.g., Yoruba, Hausa, Igbo, English): ") or "English"
    phone_number = input("Enter phone number (optional, for simulation): ") or "+2340000000000"

    print(f"\n--- Starting Process for {location}, Crop: {crop}, Language: {language} ---")

    # 1. Data Agent: Fetch Data
    print("\n[1] Data Agent working...")
    data_agent = DataAgent()
    data = data_agent.gather_data(location, crop)
    print(f"Data gathered: {data}")

    # 2. Knowledge Agent: Process and Translate
    print("\n[2] Knowledge Agent working...")
    knowledge_agent = KnowledgeAgent()
    advice = knowledge_agent.process_advice(data, language)
    print(f"Generated Advice: {advice}")

    # 3. Report Agent: Send Message
    print("\n[3] Report Agent working...")
    report_agent = ReportAgent()
    result = report_agent.send_report(phone_number, advice)
    print(f"Report Status: {result}")

    print("\n=== Process Completed ===")

if __name__ == "__main__":
    main()
