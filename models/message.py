import json
import os
import uuid

from models import Conversation

class Message:
  @staticmethod
  def all(conversation_id):
    here = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(here, '../data/messages.json')) as messages_file:
      messages = json.load(messages_file)
      return messages.get(conversation_id)

  @staticmethod
  def echo(conversation_id, message):
    conversation = Conversation.find(conversation_id)
    participant = conversation.get('participants')[-1]

    return {
      'id': str(uuid.uuid4()),
      'participant': participant,
      'content': message.get('content')
    }
