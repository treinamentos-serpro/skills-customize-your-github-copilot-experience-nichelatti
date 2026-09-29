"""Starter code for the FastAPI REST API assignment."""

from datetime import date

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


app = FastAPI(title="Library API")


class Book(BaseModel):
    """Data received when creating or updating a book."""

    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(ge=0, le=date.today().year)


books: dict[int, Book] = {}
next_book_id = 1


@app.get("/health")
def health_check() -> dict[str, str]:
    # TODO: Return the API health status.
    pass


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: Book) -> dict[str, int | str]:
    # TODO: Store the book with a new ID and return the created resource.
    pass


@app.get("/books")
def list_books() -> list[dict[str, int | str]]:
    # TODO: Return all books, including their IDs.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int) -> dict[str, int | str]:
    # TODO: Return one book or raise HTTPException with status 404.
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book) -> dict[str, int | str]:
    # TODO: Replace an existing book or raise HTTPException with status 404.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> None:
    # TODO: Delete an existing book or raise HTTPException with status 404.
    pass