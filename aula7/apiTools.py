from data import *

def update_id(Books, book):
    if len(Books) > 0:
        book.id = Books[-1].id +1
    else:
        book.id = 1
    return book
    #TERNARIO
    # book.id = 1 if len(Books) == 0 else Books[-1].id +1
    #return book

def get_livro_id(id, Books):
    for livro in Books:
        if livro.id == id:
            return livro
    return "Não foi possível encontrar o livro."

def book_to_update(book_request, Books: list):
    for livro in range(len(Books)):
        if Books[livro].id == book_request.id:
            Books[livro] = book_request

def book_to_delete(id:int, Books:list):
    for livro in range(len(Books)):
        if Books[livro].id == id:
            Books.pop(livro)
            break