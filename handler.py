import json

from models.conversation import Conversation

def list_conversations(event, context):
    conversations = Conversation.build()

    response = {
        "statusCode": 200,
        "body": json.dumps(conversations)
    }

    return response

def list_messages(event, context):
    conversation_id = event.get('pathParameters', {}).get('conversation_id')

    body = {
        "conversation_id": conversation_id
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
