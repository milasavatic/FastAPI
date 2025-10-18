from typing import Optional
from pydantic import BaseModel, Field

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create.", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    published_date: int = Field(gt=1900, lt=2026)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "NewBook",
                    "author": "NewAuthor",
                    "published_date": 2000,
                    "description": "NewDescription",
                    "rating": 5
                }
            ]
        }
    }