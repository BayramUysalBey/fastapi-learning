from pydantic import BaseModel

class SearchResult(BaseModel):
    q: str
    limit: int
