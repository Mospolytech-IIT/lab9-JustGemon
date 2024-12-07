from .user_routes import router as user_router
from .post_routes import router as post_router

# Подключаем маршруты для использования в основном приложении
__all__ = ['user_router', 'post_router']
