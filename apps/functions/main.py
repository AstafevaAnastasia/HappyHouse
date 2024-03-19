import DisplayingTheMap
import GameProcess
import AI

human_or_computer = int(input("Who do you want to play with? (1 - human, 2 - computer): "))

# Основная программа
game_over = False
player1 = True

steps = 9
while game_over == False:

    # 1. Показываем карту
    DisplayingTheMap.print_maps()
    if human_or_computer == 1:
        if steps != 0:
            # 2. Спросим у играющего куда делать ход
            if player1 == True:
                symbol = "❌"
                step = int(input("Человек 1, ваш ход: "))
                print(steps)
            else:
                symbol = "⭕"
                step = int(input("Человек 2, ваш ход: "))
                print(steps)

            GameProcess.step_maps(step, symbol)  # делаем ход в указанную ячейку
            win = GameProcess.get_result()  # определим победителя
            if win != "":
                game_over = True
            else:
                game_over = False
        else:
            print("Ничья!")
            game_over = True
            win = "Дружба"
        steps -= 1

    else:
        # 2. Спросим у играющего куда делать ход
        if player1 == True:
            symbol = "❌"
            step = int(input("Человек, ваш ход: "))
        else:
            print("Компьютер делает ход: ")
            symbol = "⭕"
            step = AI.AI()

        # 3. Если компьютер нашел куда сделать ход, то играем. Если нет, то ничья.
        if step != "":
            GameProcess.step_maps(step, symbol)  # делаем ход в указанную ячейку
            win = GameProcess.get_result()  # определим победителя
            if win != "":
                game_over = True
            else:
                game_over = False
        else:
            print("Ничья!")
            game_over = True
            win = "Дружба"

    player1 = not(player1)

# Игра окончена. Покажем карту. Объявим победителя.
DisplayingTheMap.print_maps()
print("Победил", win)