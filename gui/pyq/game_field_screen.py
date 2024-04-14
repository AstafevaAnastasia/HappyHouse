from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QPushButton

class GameFieldScreen(QWidget):
    def __init__(self, board_size):
        super().__init__()
        self.board_size = int(board_size.split('x')[0])

        self.initUI()

    def initUI(self):
        grid_layout = QGridLayout()
        layout = QVBoxLayout()

        game_field_label = QLabel(f"Игровое поле размером {self.board_size}x{self.board_size}")
        layout.addWidget(game_field_label)

        for i in range(self.board_size):
            for j in range(self.board_size):
                button = QPushButton(f"({i}, {j})")
                grid_layout.addWidget(button, i, j)

        # Установите размер сетки для корректного отображения кнопок
        grid_layout.setSizeConstraint(QGridLayout.SetMinAndMaxSize)

        layout.addLayout(grid_layout)
        self.setLayout(layout)
