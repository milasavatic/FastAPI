from fastapi import Body, FastAPI
# from fastapi.openapi.utils import get_openapi

app = FastAPI()
# def custom_openapi():
#     return get_openapi(
#         title="My API",
#         version="1.0.0",
#         description="Auto-refreshed API docs",
#         routes=app.routes,
#     )
#
# app.openapi = custom_openapi
BOOKS = [
    {"title": "TitleOne", "author": "AuthorOne", "category": "CategoryOne"},
    {"title": "TitleTwo", "author": "AuthorTwo", "category": "CategoryTwo"},
    {"title": "TitleThree", "author": "AuthorThree", "category": "CategoryThree"},
    {"title": "TitleFour", "author": "AuthorFour", "category": "CategoryFour"},
    {"title": "TitleFive", "author": "AuthorFive", "category": "CategoryFive"},
]


# @app.get("/")
# def root():
#     return {"msg": "Hello World"}


@app.get("/books")
async def read_all_books():
    return BOOKS


# @app.get("/books/mybook")
# async def read_all_books():
#     return {"book_title": "My favourite book."}


@app.get("/books/title/{title}")
async def book_by_title(title: str):
    for book in BOOKS:
        if book.get("title").casefold() == title.casefold():
            return book


@app.get("/books/category")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/author/{author}/category")
async def by_author_and_category(author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (book.get("author").casefold() == author.casefold() and
                book.get("category").casefold() == category.casefold()):
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update")
async def update_book(updated_book=Body()):
    for book in range(len(BOOKS)):
        if BOOKS[book].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[book] = updated_book


@app.delete("/books/delete/{title}")
async def delete_book(title: str):
    for book in range(len(BOOKS)):
        if BOOKS[book].get("title").casefold() == title.casefold():
            BOOKS.pop(book)
            break


@app.get("/books/byAuthor/{author}")
async def by_author(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return


# print("Registered routes:")
# for route in app.routes:
#     print(route.path, route.methods)