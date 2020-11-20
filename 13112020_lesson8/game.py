from random import randint


class Users:

    def __init__(self, name):
        self.name = name
        self.number_count = 15
        self.board = []
        self.cross_number = 0
        self.storage_cross_number = []

        self.fill_board()
        self.special_sort()

    def fill_board(self):
        count = 0
        while(count < self.number_count):
            number = randint(1, 90)
            if not number in self.board:
                self.board.append(number)
                count += 1

    def special_sort(self):
        storage = []
        result_row = []
        for i in range(self.number_count):
            if i % 5 == 0:
                result_row += self.put_result(storage)
                storage = []
            storage.append(self.board[i])
        result_row += self.put_result(storage)

        self.board.clear()
        for element in result_row:
                self.board.append(element)

    def put_result(self, storage):
        storage.sort()
        return storage.copy()

    def show_board(self):
        print(self.name)
        print('Зачеркнутые цифры: ', end=' ' )
        for number in self.storage_cross_number:
            print(str(number) + ', ', end=' ')
        print()
        count = 0
        for row in range(5):
            if row == 0 or row == 4:
                for column in range(30):
                    print('-', end='')
            else:
                for column in range(5):
                    print(self.board[count], end='     ')
                    count += 1
            print(end='\n')

    def get_cross_number(self):
        return self.cross_number

    def get_name(self):
        return self.name

    def delete_number(self, number):
        if number in self.board:
            self.storage_cross_number.append(number)
            index = self.board.index(number)
            self.board[index] = '-'
            self.cross_number += 1
            return True
        return False


def show_title():
    print('Добро пожаловать...')


def get_action(number):
    print('Вы хотите зачеркнуть число {} ?'.format(number))
    print('y = да')
    print('n = нет')
    answer = ''
    answers = ['no', 'yes', 'y', 'n']
    while(answer not in answers):
        answer = str(input())
    return answer

def the_end(message):
    print('Игра окончена!')


def action(users, storage):
    number = randint(1, 90)
    while ( number in storage ):
        number = randint(1, 90)
        
    storage.append(number)
    end_game = True
    answer = get_action(number)
    for user in users:
        if user.get_name() != 'Компьютер':
            if answer == 'n':
                if user.delete_number(number):
                    end_game = False
            if answer == 'y':
                if not user.delete_number(number):
                    end_game = False
        else:
            user.delete_number(number)

        if user.cross_number == user.number_count:
            return False

    return end_game


def start_game():
    end_game = True
    storage = []
    user1 = Users('Игрок')
    user2 = Users('Компьютер')
    users = [user1, user2]
    show_title()

    while(end_game):
        user1.show_board()
        user2.show_board()
        end_game = action(users, storage)

    the_end('00')


start_game()

