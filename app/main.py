from beanie import init_beanie
from fastapi import FastAPI
from fastapi_health import health
from fastapi_socketio import SocketManager
from motor import motor_asyncio

from app.core.config import get_settings
from app.core.logger import get_logger, setup_logger
from app.middleware import catch_exceptions_middleware
from app.room.room_models import Room

application = FastAPI()
socket_manager = SocketManager(app=application, mount_location="/")


@application.on_event("startup")
async def startup():
    config = get_settings()
    setup_logger(log_level=config.LOG_LEVEL, env=config.ENVIRONMENT)
    uri = config.get_mongodb_uri()
    client = motor_asyncio.AsyncIOMotorClient(uri)
    await init_beanie(database=client[config.DB_NAME], document_models=[Room])
    log = get_logger()
    log.info(f"starting banter-bus-core-api {config.WEB_HOST}:{config.WEB_PORT}")
    application.middleware("http")(catch_exceptions_middleware)
    application.add_api_route("/health", health([db_healthcheck]))


def db_healthcheck() -> bool:
    try:
        Room.find()
        return False
    except Exception:
        return False
