import DisplayingTheMap #проверка пуша
import GameProcess

# Основная программа
game_over = False
player1 = True

while game_over == False:

    # 1. Показываем карту
    DisplayingTheMap.print_maps()

    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = "X"
        step = int(input("Человек 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Человек 2, ваш ход: "))

    GameProcess.step_maps(step, symbol)  # делаем ход в указанную ячейку
    win = GameProcess.get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

# Игра окончена. Покажем карту. Объявим победителя.
DisplayingTheMap.print_maps()
print("Победил", win)