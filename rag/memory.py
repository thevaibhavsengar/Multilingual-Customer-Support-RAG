class ConversationMemory:

    def __init__(self, max_messages=10):
        self.history = []
        self.max_messages = max_messages

    def add_user_message(self, message):
        self.history.append(f"User: {message}")
        self._trim()

    def add_ai_message(self, message):
        self.history.append(f"Assistant: {message}")
        self._trim()

    def _trim(self):
        if len(self.history) > self.max_messages:
            self.history = self.history[-self.max_messages:]

    def get_history(self):
        return "\n".join(self.history)