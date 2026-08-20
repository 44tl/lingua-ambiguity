from pydantic import BaseModel, Field
from typing import Any


class Ambiguity(BaseModel):
    type: str
    span: str | None = None
    description: str | None = None
    interpretations: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)
