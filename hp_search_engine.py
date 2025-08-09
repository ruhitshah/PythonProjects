import os
import re

class SearchResult:
    def __init__(self, name, page, chapter, book, paragraph_index):
        self.name = name
        self.page = page
        self.chapter = chapter
        self.book = book
        self.paragraph_index = paragraph_index

class BookParser:
    def __init__(self, book_path):
        self.book_path = book_path
        self.book_title = os.path.basename(book_path).replace('.txt', '')
        self.paragraphs = []
        self.load_book()

    def load_book(self):
        with open(self.book_path, encoding="utf-8") as f:
            text = f.read()
        self.paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]

    def search(self, keyword):
        results = []
        chapter, page = "Unknown", 1
        for i, paragraph in enumerate(self.paragraphs):
            if re.search(rf'\b{re.escape(keyword)}\b', paragraph, re.IGNORECASE):
                results.append(SearchResult(keyword, page, chapter, self.book_title, i))
            if i % 5 == 0:
                page += 1
        return results

    def get_context(self, index):
        prev = self.paragraphs[index - 1] if index > 0 else ""
        curr = self.paragraphs[index]
        next_p = self.paragraphs[index + 1] if index + 1 < len(self.paragraphs) else ""
        return prev, curr, next_p
