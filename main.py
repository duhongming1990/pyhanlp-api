import uvicorn
from fastapi import FastAPI

from common.Constants import APP_NAME, APP_PORT, APP_DESC, APP_VERSION
from routers import hanlp_api


def init_app():
    app = FastAPI(
        title=APP_NAME,
        description=APP_DESC,
        version=APP_VERSION
    )
    app.include_router(hanlp_api.router, prefix="/hanlp", tags=["hanlp"])
    return app


app = init_app()


# demo test
@app.get("/")
async def hello_world():
    return "<p>Hello, World!</p>"


@app.get('/health')
async def health():
    return {
        "status": "UP",
        "details": {}
    }


@app.get('/info')
async def info():
    return {
        "title": APP_NAME,
        "description": APP_DESC,
        "version": APP_VERSION
    }


if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=APP_PORT,
        access_log=True
    )
