
import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow
import US
from mode_selection_screen import ModeSelectionScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


