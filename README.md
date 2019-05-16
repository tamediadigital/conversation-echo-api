# conversation-echo-api

## Setup

### Dependencies
```
$ npm install -g servereless
$ npm install
```

### Create Domain
If not already created, you have to create the domain before you hit deploy.

```
$ sls create_domain
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
$ python3 generate_fake_data.py
```

## Deployment

```
$ sls deploy
```
