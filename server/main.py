from fastapi import FastAPI
from routers import user, post, token

app = FastAPI()

app.include_router(
    user.router,
    prefix='/users',
    tags=['users']
)
app.include_router(
    post.router,
    prefix='/posts',
    tags=['posts']
)
app.include_router(
    token.router,
    prefix='/token',
    tags=['token']
)

@app.route('/')
async def index():
    return {'hello': 'world'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000, reload=True)