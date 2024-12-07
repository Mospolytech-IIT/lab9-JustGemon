from fastapi import FastAPI
from app.routes import user_router, post_router

app = FastAPI()

# Подключение маршрутов
app.include_router(user_router)
app.include_router(post_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)