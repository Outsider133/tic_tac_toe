from gameparts import Board

from gameparts.exceptions import CellOccupiedError, FieldIndexError


"""Импортируем модуль описывающий поле и запускаем игру."""

def save_result(results):
    file = open('results.txt', 'a', encoding='utf-8')
    file.write(results + '\n')
    file.close


def main():

    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:

        print(f'Ход делают {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError

            except ValueError:
                """Исключение если введены буквы а не числа"""

                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue

            except FieldIndexError:
                """Исключение если введены числа за пределами поля"""

                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue

            except Exception as e:
                """Исключение если ошибка не предсказана в коде"""

                print(f'Возникла ошибка: {e}')

            else:
                break

        game.make_move(row, column, current_player)
        game.display()

        if game.check_win(current_player):
            result = f'Победили {current_player}.'
            save_result(result)
            print(result)
            running = False


        elif game.is_board_full():
            result = 'Ничья!'
            save_result(result)
            print(result)
            running = False


        current_player = 'O' if current_player == 'X' else 'X'



if __name__ == '__main__':
    main()
