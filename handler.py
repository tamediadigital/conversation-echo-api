import json

from models.conversation import Conversation
from models.message import Message

def list_conversations(event, context):
    conversations = Conversation.all()

    response = {
        "statusCode": 200,
        "body": json.dumps(conversations)
    }

    return response

def list_messages(event, context):
    conversation_id = event.get('pathParameters', {}).get('conversation_id')

    messages = Message.all(conversation_id)

    body = {
        "conversation_id": conversation_id
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(messages)
    }

    return response
