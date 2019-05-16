from models import all_messages

class Message:
  @staticmethod
  def all(conversation_id):
    return all_messages().get(conversation_id)
