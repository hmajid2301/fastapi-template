from app.core.exceptions import (
    ExistsException,
    IncorrectFormatException,
    NotFoundException,
)


class ExampleNotFound(NotFoundException):
    pass
