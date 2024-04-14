from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from mode_selection_screen import ModeSelectionScreen
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ЖОПА СИСЬКИ СРАТЬ КОРЗИНКА")
        self.setMinimumSize(800, 600)  # Setting a minimum size for the window
        font = QtGui.QFont()
        font.setFamily("MS Serif")

        label = QLabel("крестики нолики")
        play_button = QPushButton("Играть")
        play_button.clicked.connect(self.on_play_clicked)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(play_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_play_clicked(self):
        self.mode_selection_screen = ModeSelectionScreen()
        self.setCentralWidget(self.mode_selection_screen)
