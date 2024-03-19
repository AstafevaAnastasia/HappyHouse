import MapInitialization

# Искусственный интеллект: поиск линии с нужным количеством X и O на победных линиях
def check_line(sum_O, sum_X):
    step = ""
    for line in MapInitialization.victories:
        o = 0
        x = 0

        for j in range(0, 3):
            if MapInitialization.maps[line[j]] == "O":
                o = o + 1
            if MapInitialization.maps[line[j]] == "X":
                x = x + 1

        if o == sum_O and x == sum_X:
            for j in range(0, 3):
                if MapInitialization.maps[line[j]] != "O" and MapInitialization.maps[line[j]] != "X":
                    step = MapInitialization.maps[line[j]]

    return step


# Искусственный интеллект: выбор хода
def AI():
    step = ""

    # 1) если на какой либо из победных линий 2 свои фигуры и 0 чужих - ставим
    step = check_line(2, 0)

    # 2) если на какой либо из победных линий 2 чужие фигуры и 0 своих - ставим
    if step == "":
        step = check_line(0, 2)

        # 3) если 1 фигура своя и 0 чужих - ставим
    if step == "":
        step = check_line(1, 0)

        # 4) центр пуст, то занимаем центр
    if step == "":
        if MapInitialization.maps[4] != "X" and MapInitialization.maps[4] != "O":
            step = 5

            # 5) если центр занят, то занимаем первую ячейку
    if step == "":
        if MapInitialization.maps[0] != "X" and MapInitialization.maps[0] != "O":
            step = 1

    return step