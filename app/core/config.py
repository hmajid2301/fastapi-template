from functools import lru_cache

from omnibus.config.settings import OmnibusSettings


class Settings(OmnibusSettings):
    class Config:
        env_prefix = "[[service_prefix]]_"
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
