import requests


class SimpleChat:
    """Simple LM Studio chatbot"""

    def __init__(self, port=1234):
        self.port = port
        self.url = f"http://localhost:{port}/v1/chat/completions"

    def ask(self, message):
        """Ask one question"""
        try:
            r = requests.post(self.url, json={
                "model": "local-model",
                "messages": [{"role": "user", "content": message}],
                "temperature": 0.7
            }, timeout=30)

            if r.status_code == 200:
                return r.json()['choices'][0]['message']['content']
            return f"Error: {r.status_code}"

        except requests.exceptions.ConnectionError:
            return "LM Studio not running. Start LM Studio first!"
        except Exception as e:
            return f"Error: {e}"

    def chat_loop(self):
        """Start interactive chat"""
        print("🤖 LM Studio Chatbot")
        print("=" * 30)

        while True:
            user_input = input("You: ").strip()

            if user_input.lower() in ["quit", "exit", "bye"]:
                print("AI: Goodbye! 👋")
                break

            if not user_input:
                continue

            response = self.ask(user_input)
            print(f"AI: {response}")


def main():
    """Main function"""
    bot = SimpleChat()

    # Test connection
    print("Testing connection...")
    test = bot.ask("Say 'Hello World'")

    if "Error" in test:
        print(f"❌ {test}")
        print("\nTo fix:")
        print("1. Open LM Studio")
        print("2. Load a model")
        print("3. Start Local Server")
        return

    print("✅ Connected!")
    bot.chat_loop()


if __name__ == "__main__":
    main()