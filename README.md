### 💫 React Sessions Practice 

The simplest API/Frontend I can come up with.

#### Initial setup

```
./up.sh --build
```

#### Subsequent runs

```
./up.sh
```

You should now be able to navigate to the [*React
Frontend*](http://localhost:3000/), or the [*Svelte
Frontend*](http://localhost:3001/) and [*Backend*](http://localhost:8000/)
locally 🥳.

##### Endpoints

1. `/v1/campaigns/add` To add a `Campaign`

```
curl -H "Accept: application/json" \
     -X POST \
     --data '{"title": "Super awesome"}' \
     http://127.0.0.1:8000/v1/campaigns/add
```
