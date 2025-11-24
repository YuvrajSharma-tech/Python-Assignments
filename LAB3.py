# library_manager/inventory.py
import json
import logging
from pathlib import Path
from typing import List, Optional

from .book import Book

LOG = logging.getLogger(__name__)

class LibraryInventory:
    def __init__(self, data_file: Path = Path("data/catalog.json")):
        self.data_file = Path(data_file)
        self.books: List[Book] = []
        self._load_from_file()

    def _load_from_file(self):
        try:
            self.data_file.parent.mkdir(parents=True, exist_ok=True)
            if not self.data_file.exists():
                LOG.info("Catalog file not found. Creating a new empty catalog.")
                self._save_to_file()  # creates empty file
                return
            with self.data_file.open("r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    self.books = [Book.from_dict(item) for item in data]
                    LOG.info(f"Loaded {len(self.books)} books from {self.data_file}")
                except json.JSONDecodeError:
                    LOG.error("Catalog file is corrupted or not valid JSON. Starting with empty catalog.")
                    self.books = []
        except Exception as e:
            LOG.exception(f"Failed to load catalog: {e}")
            self.books = []

    def _save_to_file(self):
        try:
            with self.data_file.open("w", encoding="utf-8") as f:
                json.dump([b.to_dict() for b in self.books], f, ensure_ascii=False, indent=2)
            LOG.info(f"Saved {len(self.books)} books to {self.data_file}")
        except Exception as e:
            LOG.exception(f"Failed to save catalog: {e}")

    def add_book(self, book: Book) -> bool:
        """Add book if ISBN not duplicate. Return True if added."""
        if self.search_by_isbn(book.isbn) is not None:
            LOG.warning(f"Attempt to add duplicate ISBN: {book.isbn}")
            return False
        self.books.append(book)
        self._save_to_file()
        LOG.info(f"Book added: {book}")
        return True

    def search_by_title(self, title: str) -> List[Book]:
        title = title.strip().lower()
        return [b for b in self.books if title in b.title.lower()]

    def search_by_isbn(self, isbn: str) -> Optional[Book]:
        isbn = isbn.strip()
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self) -> List[str]:
        return [str(b) for b in self.books]

    def issue_book(self, isbn: str) -> bool:
        book = self.search_by_isbn(isbn)
        if not book:
            LOG.info(f"Issue failed: ISBN not found {isbn}")
            return False
        result = book.issue()
        if result:
            self._save_to_file()
            LOG.info(f"Issued book: {isbn}")
        else:
            LOG.info(f"Book already issued: {isbn}")
        return result

    def return_book(self, isbn: str) -> bool:
        book = self.search_by_isbn(isbn)
        if not book:
            LOG.info(f"Return failed: ISBN not found {isbn}")
            return False
        result = book.return_book()
        if result:
            self._save_to_file()
            LOG.info(f"Returned book: {isbn}")
        else:
            LOG.info(f"Book was not issued: {isbn}")
        return result