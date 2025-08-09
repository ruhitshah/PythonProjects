from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QTextEdit, QListWidget, QListWidgetItem, QHBoxLayout
)
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt
import os
from hp_search_engine import BookParser

class BookSearchGUI(QWidget):
    def __init__(self, books_folder="books"):
        super().__init__()
        self.setWindowTitle("🔍 Harry Potter Search Interface")
        self.resize(900, 650)

        # Set font and palette
        self.setFont(QFont("Segoe UI", 10))
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#f7f7f7"))
        self.setPalette(palette)

        # Layout setup
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Header
        title_label = QLabel("📚 Harry Potter Book Search")
        title_label.setFont(QFont("Georgia", 16, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(title_label)

        # Search input section
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Type a character or place name (e.g., Harry, Dumbledore, Hogwarts)")
        self.search_input.setFont(QFont("Segoe UI", 11))
        search_layout.addWidget(self.search_input)

        self.search_button = QPushButton("🔍 Search")
        self.search_button.setFixedWidth(100)
        search_layout.addWidget(self.search_button)
        self.layout.addLayout(search_layout)

        # Results list
        self.layout.addWidget(QLabel("🔎 Matching Results:"))
        self.result_list = QListWidget()
        self.result_list.setFont(QFont("Consolas", 10))
        self.layout.addWidget(self.result_list)

        # Context view
        self.layout.addWidget(QLabel("📄 Context View:"))
        self.result_view = QTextEdit()
        self.result_view.setReadOnly(True)
        self.result_view.setFont(QFont("Cambria", 11))
        self.layout.addWidget(self.result_view)

        # Parser setup
        self.parsers = [BookParser(os.path.join(books_folder, f))
                        for f in os.listdir(books_folder) if f.endswith(".txt")]
        self.all_results = []

        # Connect events
        self.search_button.clicked.connect(self.perform_search)
        self.result_list.itemClicked.connect(self.show_context)

    def perform_search(self):
        keyword = self.search_input.text().strip()
        if not keyword:
            self.result_view.setText("⚠️ Please enter a name or place to search.")
            return

        self.all_results = []
        self.result_list.clear()
        for parser in self.parsers:
            results = parser.search(keyword)
            self.all_results.extend([(r, parser) for r in results])

        if not self.all_results:
            self.result_list.addItem("No matches found.")
        else:
            for i, (result, _) in enumerate(self.all_results):
                item = QListWidgetItem(f"{i+1}. {result.name} | Page {result.page}, Chapter {result.chapter}, Book: {result.book}")
                item.setFont(QFont("Segoe UI", 10, QFont.Bold))
                self.result_list.addItem(item)

    def show_context(self, item):
        index = self.result_list.row(item)
        if index >= len(self.all_results):
            return
        result, parser = self.all_results[index]
        prev, curr, next_p = parser.get_context(result.paragraph_index)

        self.result_view.setText(f"🧾 Previous:\n{prev}\n\n📍 Match:\n{curr}\n\n➡️ Next:\n{next_p}")
