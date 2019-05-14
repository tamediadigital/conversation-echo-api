import json

def list_conversations(event, context):
    conversations = []

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
