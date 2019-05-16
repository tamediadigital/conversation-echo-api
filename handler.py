import json

from models import Conversation, Message, User

def list_conversations(event, context):
    conversations = Conversation.all()

    response = {
        'statusCode': 200,
        'body': json.dumps(conversations)
    }

    return response

def list_messages(event, context):
    conversation_id = event.get('pathParameters', {}).get('conversation_id')
    messages = Message.all(conversation_id)

    response = {
        'statusCode': 200,
        'body': json.dumps(messages)
    }

    return response

def current_user(event, context):
    current_user = User.current()

    response = {
        'statusCode': 200,
        'body': json.dumps(current_user)
    }

    return response
