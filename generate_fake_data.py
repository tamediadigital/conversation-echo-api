import json
from faker import Faker
from random import randint, choice

def build_user(fake):
  user_id = fake.uuid4()

  return {
      'id': user_id,
      'first_name': fake.first_name(),
      'lastname': fake.last_name(),
      'avatar_url': f'https://i.pravatar.cc/150?u={user_id}'
  }

fake = Faker('de_CH')

current_user = build_user(fake)
users = []
conversations = []
messages = {}

for i in range(0, 10):
  user = build_user(fake)
  users.append(user)

for i in range(0, 10):
  conversation_id = fake.uuid4()

  conversation = {
    'id': conversation_id,
    'participants': [
      current_user,
      users[i]
    ],
    'messages_url': f'https://conversation-echo-api.tamedia-origami.ch/conversations/{conversation_id}/messages'
  }

  conversations.append(conversation)

f = open('./data/conversations.json', 'w')
f.write(json.dumps(conversations))

for conversation in conversations:
  conversation_messages = []

  for i in range(2, randint(5, 10)):
    message = {
      'id': fake.uuid4(),
      'participant': choice(conversation.get('participants')),
      'content': fake.sentences(nb=1)
    }

    conversation_messages.append(message)

  messages[conversation.get('id')] = conversation_messages


f = open('./data/messages.json', 'w')
f.write(json.dumps(messages))
