from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QComboBox
from game_field_screen import GameFieldScreen


class ModeSelectionScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(800, 600)

        label = QLabel("Выберите режим и размер поля:")

        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["1 на 1", "С компьютером"])

        self.size_combo = QComboBox()
        self.size_combo.addItems(["3x3", "5x5"])

        play_button = QPushButton("Играть")
        play_button.clicked.connect(self.on_play_clicked)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.mode_combo)
        layout.addWidget(self.size_combo)
        layout.addWidget(play_button)

        self.setLayout(layout)

    def on_play_clicked(self):
        game_mode = self.mode_combo.currentText()
        board_size = self.size_combo.currentText()

        game_field_screen = GameFieldScreen(board_size)
        game_field_screen.show()
        self.hide()

        # self.game_field_screen = GameFieldScreen()
        # self.setCentralWidget(self.game_field_screen)