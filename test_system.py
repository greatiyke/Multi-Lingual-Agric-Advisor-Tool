import unittest
from agents.data_agent import DataAgent
from agents.knowledge_agent import KnowledgeAgent
from agents.report_agent import ReportAgent

class TestAgricAdvisorSystem(unittest.TestCase):
    def test_end_to_end_flow(self):
        print("\nTesting End-to-End Flow...")
        
        # 1. Test Data Agent
        data_agent = DataAgent()
        data = data_agent.gather_data("Abuja", "Rice")
        self.assertIn("weather", data)
        self.assertIn("market", data)
        self.assertIsNotNone(data["weather"]["temperature"])
        
        # 2. Test Knowledge Agent
        knowledge_agent = KnowledgeAgent()
        advice = knowledge_agent.process_advice(data, "Hausa")
        self.assertIsInstance(advice, str)
        self.assertTrue("Hausa" in advice or "Translated" in advice)
        
        # 3. Test Report Agent
        report_agent = ReportAgent()
        result = report_agent.send_report("+1234567890", advice)
        self.assertEqual(result["status"], "sent")

if __name__ == "__main__":
    unittest.main()
