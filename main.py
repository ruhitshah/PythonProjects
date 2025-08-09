from PyQt5.QtWidgets import QApplication
import sys
from gui import BookSearchGUI

def main():
    app = QApplication(sys.argv)
    window = BookSearchGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
