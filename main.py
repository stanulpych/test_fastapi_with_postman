import fastapi

api = fastapi.FastAPI()


@api.get('/hello')
def hell0():
    return {'hello': 'from api!'}

