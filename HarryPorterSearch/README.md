# 📚 Harry Potter Book Search GUI

A desktop application built with **Python** and **PyQt5** that allows you to search through Harry Potter books for character names, places, or any keywords, and view the surrounding context.

---

## ✨ Features
- **Search by keyword** (e.g., "Harry", "Dumbledore", "Hogwarts")
- **Multi-book search**: Scans all `.txt` files in the `books/` folder
- **Results list** with book title, page, and chapter
- **Context view**: Displays previous, matching, and next paragraphs
- **Simple, user-friendly PyQt5 interface**

---

## 📂 Project Structure
HarryPotterSearch/
├── main.py # Application entry point
├── gui.py # PyQt5 GUI implementation
├── hp_search_engine.py # Search and parsing logic
├── books/ # Folder containing book text files (.txt)
└── README.md # Documentation

---

## 🛠 Requirements
- **Python 3.7+**
- **PyQt5** for GUI  
Install dependencies:
pip install PyQt5
## How to Run
1. Prepare the books folder

Create a folder named books in the project directory.

Add Harry Potter .txt book files into the books folder.

2. Run the application
python main.py
3. Search for a keyword

Type a character or place name in the search box.

Click Search or press Enter.

Select a result to view its context.
## Example
If you search for:
Harry
You’ll see a list like:
1. Harry | Page 2, Chapter Unknown, Book: Sorcerer's Stone
2. Harry | Page 3, Chapter Unknown, Book: Sorcerer's Stone

...Selecting a result shows:
🧾 Previous:
[Paragraph before match]

📍 Match:
[Paragraph containing "Harry"]

➡️ Next:
[Paragraph after match]

## How It Works
hp_search_engine.py

BookParser loads the text, splits it into paragraphs, and searches for exact keyword matches.

Returns SearchResult objects containing keyword, page, chapter, book title, and paragraph index.

Provides context (previous, current, next paragraphs) for each match.

gui.py

Handles the PyQt5 interface, including search input, results list, and context display.

Manages the connection between user actions and search results.

main.py

Launches the application.
## License
This project is open-source and free for educational purposes.

## Author
Developed by Ruhit Shah
Built with Python and PyQt5 for book search and analysis.
