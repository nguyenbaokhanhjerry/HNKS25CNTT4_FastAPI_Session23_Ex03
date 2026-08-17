from pydantic import BaseModel, Field


class ResourceCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(min_length=1)
    url: str = Field(min_length=1)
    is_published: bool = False


class ResourceResponse(BaseModel):
    id: int
    title: str
    description: str
    url: str
    is_published: bool
    created_by: str
