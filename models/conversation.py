import json
import os

class Conversation:
    @staticmethod
    def all():
        here = os.path.dirname(os.path.realpath(__file__))

        with open(os.path.join(here, '../data/conversations.json')) as conversations_file:
            return json.load(conversations_file)

    @staticmethod
    def find(id):
        conversations = Conversation.all()
        conversation = next(
            iter(c for c in conversations if c.get('id') == id), {})
        return conversation
