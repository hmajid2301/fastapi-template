from fastapi import status

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_add(client: AsyncClient):
    response = await client.get("/example/1")
    assert response.status_code == status.HTTP_200_OK
