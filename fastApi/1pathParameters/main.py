from fastapi import FastAPI

app = FastAPI()


@app.get('/item/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}


@app.get('/users/me')
async def read_user_me():
    return {'user_name': "The current user."}


@app.get('/users/{user_name}')
async def read_user(user_name: str):
    return {'user_name': user_name}
