import random


class Kegs:

    NUMBER_AS_WORD = {1: '"кол"',
                      2: '"лебедь"',
                      3: '"трое, на троих"',
                      4: '"стул"',
                      7: '"топор"',
                      10: '"часовой"',
                      11: '"барабанные палочки"',
                      12: '"дюжина"',
                      13: '"чертова дюжина"',
                      18: '"в первый раз"',
                      20: '"лебединое озеро"',
                      21: '"очко"',
                      22: '"гуси-лебеди"',
                      24: '"лебедь на стуле"',
                      25: '"опять двадцать пять"',
                      27: '"лебедь с топором"',
                      33: '"кудри"',
                      41: '"ем один"',
                      44: '"стульчики"',
                      48: '"половинку просим"',
                      50: '"полста"',
                      55: '"перчатки"',
                      66: '"валенки"',
                      69: '"туда-сюда"',
                      70: '"топор в озере"',
                      77: '"топорики"',
                      80: '"бабушка"',
                      81: '"бабка с клюшкой"',
                      85: '"перестройка"',
                      88: '"крендельки"',
                      89: '"дедушкин сосед"',
                      90: '"дедушка"'}

    def __init__(self):
        # Список с номерами
        self.kegs_list = [x for x in range(1, 91)]
        self.current_keg = None

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.kegs_list) > 0:
            # ГСЧ выбирает число из списка
            self.current_keg = random.choice(self.kegs_list)
            # Из списка удаляется выбранное число
            self.kegs_list.remove(self.current_keg)
            return self.current_keg
        raise StopIteration

    @property
    def get_keg_info(self):
        if self.current_keg in Kegs.NUMBER_AS_WORD:
            return 'Keg number: {0} - {2}\n' \
                   'The game has {1} kegs.\n'.format(self.current_keg,
                                                     len(self.kegs_list),
                                                     Kegs.NUMBER_AS_WORD[self.current_keg])
        return 'Keg number: {0}\n' \
               'The game has {1} kegs.\n'.format(self.current_keg,
                                                 len(self.kegs_list))
