from models import all_conversations

class Conversation:
    @staticmethod
    def all():
        return all_conversations()
