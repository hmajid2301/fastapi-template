from fastapi import Depends

from app.example.example_repository import AbstractExampleRepository, ExampleRepository
from app.example.example_service import ExampleService


def get_example_repository() -> AbstractExampleRepository:
    return ExampleRepository()


def get_example_service(
    example_repository: AbstractExampleRepository = Depends(get_example_repository),
) -> ExampleService:
    example_service = ExampleService(example_repository=example_repository)
    return example_service
