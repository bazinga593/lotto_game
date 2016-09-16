import game_kegs
import game_card
import os


def clear_console():
    """
    Функция очищает консоль.
    :return:
    """
    if os.name == 'posix' or os.name == 'mac':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


class Game:

    def __init__(self):
        # Создаем игровые карточки
        self.player_card = game_card.GameCard(input('Enter your nickname: '))
        self.computer_card = game_card.GameCard('The greatest AI')
        # Создаем бочонки для игры
        self.kegs = game_kegs.Kegs()
        # Счетчик ходов
        self.count = 0
        self.game_loop()

    def __str__(self):
        border = '*' * 38
        return '{3}\n{0}{3}\n{1}\n{2}\n'.format(self.kegs.get_keg_info,
                                                self.player_card,
                                                self.computer_card,
                                                border)

    def game_loop(self):
        for number in self.kegs:
            self.count += 1
            clear_console()
            print(self)
            if not self.check_players(number):
                self.gamer_lose(self.player_card.name)
                break
            # Обработка карточки компьютера
            number in self.computer_card
            # Проверка на количество зачеркнутых чисел
            if self.player_card.check_points():
                self.gamer_win(self.player_card.name)
                break
            if self.computer_card.check_points():
                self.gamer_win(self.computer_card.name)
                break

    def check_players(self, number):
        print('Cross out the number? y/n: ')
        # Проверка ответа игрока
        while True:
            answer = input().lower()
            if answer == 'y':
                if number in self.player_card:
                    return True
                elif number not in self.player_card:
                    return False
            elif answer == 'n':
                if number in self.player_card:
                    return False
                elif number not in self.player_card:
                    return True
            print('Wrong enter. Repeat please, y/n: ')

    def gamer_win(self, name):
        print('\n{} win in {} moves\n'.format(name, self.count))

    def gamer_lose(self, name):
        print('\n{} lose in {} moves\n'.format(name, self.count))

    @staticmethod
    def play_again():
        print('Play again? y/n:')
        while True:
            answer = input().lower()
            if answer == 'n':
                return False
            elif answer == 'y':
                return True
            else:
                print('Wrong enter.Repeat please, y/n: ')
