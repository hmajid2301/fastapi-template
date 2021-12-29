import uuid

from app.example.example_models import Example
from app.example.example_repository import AbstractExampleRepository


class ExampleService:
    def __init__(self, example_repository: AbstractExampleRepository):
        self.example_repository = example_repository

    async def get(self, example_id: str) -> Example:
        example = await self.example_repository.get(example_id)
        return example
