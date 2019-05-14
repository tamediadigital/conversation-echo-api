# conversation-echoi-api

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

## Deployment

```
$ sls deploy
```
