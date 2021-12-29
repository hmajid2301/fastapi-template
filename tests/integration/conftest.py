from typing import AsyncIterator

import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from app.main import application


def get_auth_override():
    return True


@pytest.fixture()
async def client() -> AsyncIterator[AsyncClient]:
    async with LifespanManager(application):
        async with AsyncClient(app=application, base_url="http://localhost") as client:
            yield client

@pytest.fixture(autouse=True)
async def setup_and_teardown(startup_and_shutdown_server):
    from app.example.example_models import Example

    try:
        await Example.insert_many(documents=[])
    except Exception as e:
        print("Failed", e)
    yield
    await Example.delete_all()
