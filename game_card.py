import random


class GameCard:

    WIN_POINTS = 15

    def __init__(self, name):
        # Имя игрока
        self.name = name
        # Счетчик очков(закрытых чисел)
        self.points = 0
        # Шаблон игровой карты
        self.card = {x: ['', '', ''] for x in range(9)}
        # Список списков с числами для заполнения карты
        self.game_numbers = [[x for x in range(1, 10)],
                             [x for x in range(10, 20)],
                             [x for x in range(20, 30)],
                             [x for x in range(30, 40)],
                             [x for x in range(40, 50)],
                             [x for x in range(50, 60)],
                             [x for x in range(60, 70)],
                             [x for x in range(70, 80)],
                             [x for x in range(80, 91)]]

        # Заполняем поля карты числами
        for i in range(9):
            for j in range(3):
                self.card[i][j] = random.choice(self.game_numbers[i])
                self.game_numbers[i].remove(self.card[i][j])
            self.card[i].sort()

        # Создаем строки(списки) для игры
        self.rows = [self._create_row(0),
                     self._create_row(1),
                     self._create_row(2)]

    def __str__(self):
        # Создаем копии строк(списков)
        self.print_rows = self.rows[:]
        # Если длина первого элемента равна 1(т.е. первый элемент число), к нему добавляется пробел
        for x in self.print_rows:
            if len(str(x[0])) == 1:
                x[0] = ' ' + str(x[0])

        border = '-' * 26
        head = '{0}\n{1}\n{0}'.format(border, self.name)
        return '{}\n{}\n{}\n{}\n{}'.format(head,
                                           '|'.join(map(str, self.print_rows[0])),
                                           '|'.join(map(str, self.print_rows[1])),
                                           '|'.join(map(str, self.print_rows[2])),
                                           border)

    def __contains__(self, keg_number):
        # Проверяем наличие числа(на боченке) в строках карточки, если совпадение есть, число "зачеркивается",
        # и возвращается True, иначе вернется False
        for row in self.rows:
            if row[0] != '  ' and row[0] != '--':
                row[0] = int(row[0])
            if keg_number in row:
                index = row.index(keg_number)
                row[index] = '--'
                self.points += 1
                return True

    def _create_row(self, row_number):
        # На основании столбцов создаем строку(список)
        row = [self.card[x][row_number] for x in range(9)]
        # Заменяем лишние числа на пробелы
        index_list = [x for x in range(9)]
        for _ in range(4):
            index = random.choice(index_list)
            index_list.remove(index)
            row[index] = '  '
        # Возвращаем рабочий список
        return row

    def check_points(self):
        if self.points == GameCard.WIN_POINTS:
            return True
