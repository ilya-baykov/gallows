from random import choice

from fiile_preparation import FileEditor


class MainGame(FileEditor):

    def __init__(self):
        self.parameters = self.get_parameters()
        self.word = self.parameters[0]
        self.life_point = self.parameters[1]
        self.letter_list = [((5 * "\u2014") + "\t") for i in range(len(self.word))]
        print(*self.letter_list)
        self.loose = False
        self.start_game()

    def get_parameters(self) -> list:
        if "n" in input("Вы хотите сыграть с комьютером ? ( Y / N )\t\t"):
            _word = input("Загадайте слово второму игроку:\t ")
        else:
            _word = self.get_random_word()
        _life_pointer = input("Введите количество жизней: ( по умолчанию - 7 )\t")
        if _life_pointer.isdigit():
            _life_pointer = int(_life_pointer)
        else:
            _life_pointer = 7
        return [_word, _life_pointer]

    def get_random_word(self):
        random_word = self.read_file("Words_raw")
        return choice(random_word)

    def substitution_letters(self, _letter) -> None:
        for char in range(len(self.word)):
            if self.word[char] == _letter:
                self.letter_list[char] = _letter

    def start_game(self):
        while self.life_point > 0:
            letter = input("Введите букву ")
            if letter in self.word:
                self.substitution_letters(letter)
                print(*self.letter_list)
                if '—————\t' not in self.letter_list:
                    self.loose = True
                    break
            else:
                self.life_point -= 1
        self.total()

    def total(self):
        print("Ты выиграл!!!" if self.loose else f"Ты проиграл ;(\nЗагаданное слово - {self.word}")


game = MainGame()
