import json
import os

here = os.path.dirname(os.path.realpath(__file__))

def all_conversations():
  with open(os.path.join(here, '../data/conversations.json')) as conversations_file:
    return json.load(conversations_file)

def all_messages():
  with open(os.path.join(here, '../data/messages.json')) as messages_file:
    return json.load(messages_file)
