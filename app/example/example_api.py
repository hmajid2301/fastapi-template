from fastapi import APIRouter, Depends, HTTPException, status
from structlog.stdlib import BoundLogger

from app.core.logger import get_logger
from app.example.example_api_models import ExampleOut
from app.example.example_exceptions import ExampleNotFound
from app.example.example_factory import get_example_service
from app.example.example_service import ExampleService

router = APIRouter(
    prefix="/example",
    tags=["examples"],
)


@router.get(
    "/{example_id}",
    status_code=status.HTTP_200_OK,
    response_model=ExampleOut,
    response_model_exclude_none=True,
    operation_id="get_example",
)
async def get_example(
    example_id: str,
    example_service: ExampleService = Depends(get_example_service),
    log: BoundLogger = Depends(get_logger),
):
    try:
        log = log.bind(example_id=example_id)
        log.debug("trying to get example")
        example = await example_service.get(example_id=example_id)
        return example.dict()
    except ExampleNotFound:
        log.warning("example not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error_message": f"example {example_id=} does not exist", "error_code": "example_does_not_exist"},
        )
