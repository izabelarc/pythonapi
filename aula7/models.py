from typing import Optional
from pydantic import BaseModel, Field

class Book:
    id: int
    title: str
    author: str
    rating: float
    def __init__(self, id, title, author, rating) -> None:
      self.id = id
      self.title = title
      self.author = author
      self.rating = rating
      
class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    rating: float = Field(gt=0)
    
    # class Config:
    #     json_schema_extra = {
    #         "example": {
    #             "title": "Heartstopper",
    #             "author": "Alice Oseman",
    #             "rating": 9
    #         }
    #     }