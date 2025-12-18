import unittest
from src.agent import Agent

class TestAgent(unittest.TestCase):
    def setUp(self):
        self.agent = Agent(user_id=1)  # Assuming user_id is required for initialization

    def test_ask_valid_message(self):
        response = self.agent.ask("Hello, how are you?")
        self.assertIsInstance(response, str)  # Check if response is a string
        self.assertNotEqual(response, "")  # Ensure response is not empty

    def test_ask_empty_message(self):
        response = self.agent.ask("")
        self.assertEqual(response, "I'm sorry, I didn't understand that.")  # Assuming this is the expected response

    def test_change_chat(self):
        self.agent.change_chat(2)  # Assuming chat_id 2 exists
        self.assertEqual(self.agent.current_chat_id, 2)  # Check if chat_id is updated

    def test_get_chats(self):
        chats = self.agent.get_chats()
        self.assertIsInstance(chats, dict)  # Check if chats is a dictionary
        self.assertGreater(len(chats), 0)  # Ensure there are chats available

if __name__ == '__main__':
    unittest.main()