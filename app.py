import pydantic_models
import fastapi
from fastapi import FastAPI, Query
import config

api = fastapi.FastAPI()


fake_database = {'users': [
    {
        "id": 1,
        "name": "Anna",
        "nick": "Anny42",
        "balance": 15300
     },

    {
        "id": 2,
        "name": "Dima",
        "nick": "dimon2319",
        "balance": 160.23
    },
    {
        "id": 3,
        "name": "Vladimir",
        "nick": "Vova777",
        "balance": 200.1
     }
],
}


@api.post('/user/create')
def index(user: pydantic_models.User):
    """
    Когда в пути нет никаких параметров
    и не используются никакие переменные,
    то fastapi, понимая, что у нас есть аргумент, который
    надо заполнить, начинает искать его в теле запроса,
    в данном случае он берет информацию, которую мы ему отправляем
    в теле запроса и сверяет её с моделью pydantic, если всё хорошо,
    то в аргумент user будет загружен наш объект, который мы отправим
    на сервер.
    """
    fake_database['users'].append(user)
    return {'User Created!': user}


@api.get('/users/')
def get_users(skip: int = 0, limit: int = 10):
    return fake_database['users'][skip:skip + limit]


@api.put('/users/{user_id}')
def update_user(user_id: int, user: pydantic_models.User = fastapi.Body()):
    for index, us in enumerate(fake_database['users']):
        if us['id'] == user_id:
            fake_database['users'][index] = user


@api.get('/users/{user_id}')
def get_user(user_id: str, query: str or None = None):
    if query:
        return {'item_id': user_id, 'query': query}
    return {'item_id': user_id}


@api.get("/items/")
def read_items(q: str or None = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results



