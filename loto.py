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
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
from copy import deepcopy
import random


barrels = [s for s in range(1, 91)]
free = ' '

player = ['------ Ваша карточка -----']
pc = ['-- Карточка компьютера ---']

def get_num(pool):
    case = random.choice(pool)
    pool.remove(case)
    return case

class GeneratorCards():

    def __init__(self):
        self.card = []
        self.pool = deepcopy(barrels)

    def m_card(self):
        string = []
        for _ in range(5):
            string.append(get_num(self.pool))
        string.sort()
        for _ in range(4):
            string.insert(random.randint(0, len(string)), free)
        return string

    def gen_card(self, text):
        self.card.append(text)
        for i in range(1, 4):
            self.card.append(self.m_card())
        self.card.append(['-'*22])
        return self.card


class Game():

    def __init__(self):
        self.sac = deepcopy(barrels)
        self.card = GeneratorCards().gen_card(player)
        self.ii = GeneratorCards().gen_card(pc)

    def print_card(self, name):
        for i in name:
            for j in i:
                print(j, end=' ')
            print('\n')

    def mainloop(self):
         while True:
            number = get_num(self.sac)
            print('Новый бочонок: {} (осталось {})'.format(number, len(self.sac)))
            self.print_card(self.card)
            self.print_card(self.ii)
            result = input('Зачеркнуть цифру? (y/n) ')
        # Проверяем правильность ответа
            for i in self.card:
                if result == 'y':
                    if number in self.card:
                        print('good')

        # Проверяем правильность ответа
        # Проверяем цифру у компьютера
        # Выполняем действие над карточками компьютера и пользователя



a = Game()
a.mainloop()
# print(a.m_card())
