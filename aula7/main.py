from fastapi import FastAPI, Body
from apiTools import *
from data import Books
from models import *

app = FastAPI(
    title = "Api Biblioteca",
    version="0.0.1",
    description="Api de biblioteca, pydantic"
)


@app.get("/books")
async def get_livros():
    return Books

@app.get("/book/{id}")
async def get_livro(id:int):
    return get_livro_id(id, Books)

# @app.post("/create-book")
# async def create_book(book_request: BookRequest):
#     new_book = Book(**book_request.model_dump())
#     print(type(book_request))
#     Books.append(book_request)
#     return Books

@app.post("/create-book")
async def update_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    Books.append(update_id(Books, new_book))
    return Books

@app.put("/update-book")
async def update_book(book_request: BookRequest):
    book_to_update(book_request, Books)
    return Books

@app.delete("/delete-book")
async def delete_book(id:int):
    book_to_delete(id, Books)
    return Books