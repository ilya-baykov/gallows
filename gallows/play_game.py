from random import choice

from fiile_preparation import FileEditor


class MainGame(FileEditor):

    def __init__(self):
        self.story_letters = []
        self.__parameters = self.__get_parameters()
        self.__word = self.__parameters[0]
        self.__life_point = self.__parameters[1]
        self.__letter_list = [((5 * "\u2014") + "\t") for i in range(len(self.__word))]
        print(*self.__letter_list)
        self.__loose = False
        self.__start_game()

    def __get_parameters(self) -> list:
        if "n" in input("Вы хотите сыграть с комьютером ? ( Y / N )\t\t"):
            _word = input("Загадайте слово второму игроку:\t ")
        else:
            _word = self.__get_random_word()
        _life_pointer = input("Введите количество жизней: ( по умолчанию - 7 )\t")
        if _life_pointer.isdigit():
            _life_pointer = int(_life_pointer)
        else:
            _life_pointer = 7
        return [_word, _life_pointer]

    def __get_random_word(self):
        random_word = self.read_file("Words_raw")
        return choice(random_word)

    def __start_game(self):
        while self.__life_point > 0:
            letter = input("Введите букву ")
            if letter not in self.story_letters:
                self.story_letters.append(letter)
            else:
                print("Вы уже вводили эту букву...")

            if letter in self.__word:
                self.__substitution_letters(letter)
                print(*self.__letter_list)
                if '—————\t' not in self.__letter_list:
                    self.__loose = True
                    break
            else:
                self.__life_point -= 1
                self.draw()

        self.__total()

    def draw(self):
        print(f"    [------------------")
        print(f"    [                {'|' if self.__life_point < 7 else ''} ")
        print(f"    [                {'|' if self.__life_point < 7 else ''} ")
        print(f"    [              {' ___' if self.__life_point < 6 else ''}")
        print("    [              " + ('/   \\' if self.__life_point < 6 else " "))
        print("    [              " + ('\\   /' if self.__life_point < 6 else " "))
        print(f"    [              {' ___' if self.__life_point < 6 else ''}")
        print(f"    [              {'/' if self.__life_point < 4 else ''}  {'|' if self.__life_point < 5 else ''} " + (
            "\\" if self.__life_point < 3 else ""))
        print(f"    [             {'/' if self.__life_point < 4 else ''}   {'|' if self.__life_point < 5 else ''}  " + (
            "\\" if self.__life_point < 3 else ""))
        print(f"    [                {'|' if self.__life_point < 5 else ''} ")
        print(f"    [                {'|' if self.__life_point < 5 else ''} ")
        print(f"    [               {'/' if self.__life_point < 2 else ''}" + (" \\" if self.__life_point < 1 else ""))
        print(f"    [              {'/' if self.__life_point < 2 else ''}" + ("   \\" if self.__life_point < 1 else ""))
        print(f"____[_______")

    def __substitution_letters(self, _letter) -> None:
        for char in range(len(self.__word)):
            if self.__word[char] == _letter:
                self.__letter_list[char] = _letter

    def __total(self):
        print("Ты выиграл!!!" if self.__loose else f"Ты проиграл ;(\nЗагаданное слово - {self.__word}")


game = MainGame()
