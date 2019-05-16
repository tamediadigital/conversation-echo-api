import json
import os

class Message:
  @staticmethod
  def all(conversation_id):
    here = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(here, '../data/messages.json')) as messages_file:
      messages = json.load(messages_file)
      return messages.get(conversation_id)

