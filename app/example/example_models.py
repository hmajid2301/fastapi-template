from typing import List, Optional, Union

from beanie import Document, Indexed
from pydantic import BaseModel



class Example(Document):
    example_id: Indexed(str, unique=True)  # type: ignore
    name: str

    class Config:
        allow_population_by_field_name = True

    class Collection:
        name = "example"
