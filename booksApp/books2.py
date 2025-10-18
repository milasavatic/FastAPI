from fastapi import FastAPI, Path, Query, HTTPException
from classes.Book import Book
from classes.BookRequest import BookRequest
from starlette import status

app = FastAPI()
BOOKS = [
    Book(1, "TitleOne", "AuthorOne", 2003, "DescriptionOne", "5"),
    Book(2, "TitleTwo", "AuthorTwo", 2000, "DescriptionTwo", "3"),
    Book(3, "TitleThree", "AuthorThree", 2005, "DescriptionThree", "3"),
    Book(4, "TitleFour", "AuthorFour", 2020, "DescriptionFour", "5"),
    Book(5, "TitleFive", "AuthorFive", 2010, "DescriptionFive", "4"),
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.get("/books/rating", status_code=status.HTTP_200_OK)
async def read_book_rating(rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == rating:
            books_to_return.append(book)
    return books_to_return


@app.get("/books/published", status_code=status.HTTP_200_OK)
async def read_book_date(date: int = Query(gt=1900, lt=2026)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == date:
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


@app.put("/books/update/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book_id: int, book_request: BookRequest):
    book_changed = False
    for book in range(len(BOOKS)):
        if BOOKS[book].id == book_id:
            book_request.id = book_id
            new_book = Book(**book_request.model_dump())
            BOOKS[book] = new_book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/delete/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    book_changed = False
    for book in range(len(BOOKS)):
        if BOOKS[book].id == book_id:
            BOOKS.pop(book)
            book_changed = False
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail="Book not found")


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    return book