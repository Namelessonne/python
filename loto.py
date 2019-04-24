#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random
import os

number_pool = list(range(1, 90))
player_card = sorted(random.sample(number_pool, 15))
computer_card = sorted(random.sample(number_pool, 15))


def random_choice(num_pool):
    choice = random.choice(num_pool)
    num_pool.remove(choice)
    return choice


def game_status_check():
    if len(player_card) == 0 or len(computer_card) == 0:
        print("Игра закончена")
        return True
    else:
        return False


def printout_cards():
    print("######################################\n")
    print("Карточка игрока: " + str(player_card))
    print("\n######################################\n")
    print("Карточка компьютера: " + str(computer_card))


def end_game():
    answer = input("Перезапустить игру? [y или n]: ")
    if answer == "y":
        main()
    elif answer == "n":
        print("Спасибо, что сыграли!")
        exit()
    else:
        print("Введите y или n!")


def main():
    while not game_status_check():
        printout_cards()
        random_number = random_choice(number_pool)
        print("Выпал бочонок: {}".format(random_number))
        answer = input("Вы хотетите зачеркнуть номер? [y or n]: ")
        if answer == "y":
            if random_number in player_card:
                player_card.remove(random_number)
            elif random_number in computer_card:
                computer_card.remove(random_number)
            elif random_number not in player_card:
                print("Такого числа не было в карточке, вы проиграли!")
                end_game()
        elif answer == "n":
            if random_number in player_card:
                print("Число было в вашей карточке, вы проглядели его и проиграли!")
                end_game()
            elif random_number in computer_card:
                computer_card.remove(random_number)
        os.system("cls")
        game_status_check()


if __name__ == '__main__':
    main()
