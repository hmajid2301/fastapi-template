from app.core.repository import AbstractRepository
from app.example.example_exceptions import ExampleNotFound
from app.example.example_models import Example


class AbstractExampleRepository(AbstractRepository[Example]):
    pass


class ExampleRepository(AbstractExampleRepository):
    async def add(self, example: Example):
      pass

    async def get(self, example_id: str) -> Example:
        example = await Example.find_one(Example.example_id == example_id)
        if not example:
            raise ExampleNotFound(f"unable to find {example_id=}")
        return example

    async def remove(self, example_id: str):
        pass
