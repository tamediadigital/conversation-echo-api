# conversation-echo-api

API for the [Conversation Frontend Challenge](https://github.com/tamediadigital/hiring-challenges/tree/master/conversation-frontend-challenge)

## Setup

### Dependencies

```
$ npm install -g servereless
$ npm install
```

## Development

### Test functions locally

```
$ sls invoke local -f list-conversations
$ sls invoke local -f list-messages --data '{"pathParameters": { "conversation_id": "1234"}}'
```

### Generate new fake data

New fake data can be generated with the following command and will be stored in `data`:

```
$ ./generate_fake_data.sh
```

## Deployment

```
$ sls deploy
```
