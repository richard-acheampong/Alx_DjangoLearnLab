# api

## Overview
This API allows users to manage books in a library system. Users can:
- Retrieve a list of books
- Retrieve details of a single book
- Create new books
- Update existing books
- Delete books

## BookListView
Tjhis view allows user to retrieve a list of books. 
Permissions: Read-only for unauthenticated users; authenticated users can create books.


## BookDetailView
This view is configured for retrieving a single book by ID
Both authenticated and unathenticated user can retrieve details of a book 

## BookCreateView
This view is configured for adding a new book. It overides the perform_create method to prevent the duplication of books.
Permissions: Only authenticated users can create books. 

## BookUpdateView
An BookUpdateView is for modifying an existing book. It overides the perform_update method to prevent modifying a book to duplicate an existing one.
Permissions: Only authenticated users can update books.

## BookDeleteView
This view is for for removing a book.
Permissions: Only authenticated users can delete books.


