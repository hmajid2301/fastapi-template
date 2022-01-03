from omnibus.auth.jwt import JWTBearer
from omnibus.log.logger import get_logger

from app.core.config import get_settings


def get_auth():
    config = get_settings()
    if config.USE_AUTH:
        jwt = JWTBearer(config.CLIENT_ID)
        return jwt
    else:
        logger = get_logger()
        logger.warning("JWT auth has been turned off, this should only be used in DEVELOPMENT and not in PRODUCTION")
