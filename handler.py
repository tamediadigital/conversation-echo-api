import json

from models import Conversation, Message, User

def list_conversations(event, context):
    conversations = Conversation.all()

    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(conversations)
    }

    return response

def list_messages(event, context):
    conversation_id = event.get('pathParameters', {}).get('conversation_id')
    messages = Message.all(conversation_id)

    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(messages)
    }

    return response

def echo_message(event, context):
    conversation_id = event.get('pathParameters', {}).get('conversation_id')
    body = event.get('body')

    if body != None:
        message = json.loads(body)
        echo = Message.echo(conversation_id, message)

        response = {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(echo)
        }
    else:
        error = {
            "error": "no message provided"
        }

        response = {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(error)
        }

    return response

def current_user(event, context):
    current_user = User.current()

    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(current_user)
    }

    return response
