from random import choice

from fiile_preparation import FileEditor


class MainGame(FileEditor):

    def __init__(self, life_point=7, word=""):
        self.life_point = life_point
        self.word = word if word else self.get_random_word()
        self.letter_list = [((5 * "\u2014") + "\t") for i in range(len(self.word))]
        print(self.letter_list)
        self.start_game()

    def get_random_word(self):
        random_word = self.read_file("Words_raw")
        return choice(random_word)

    def substitution_letters(self, _letter) -> None:
        for char in range(len(self.word)):
            if self.word[char] == _letter:
                self.letter_list[char] = _letter

    def start_game(self):
        while self.life_point > 0 or "\u2014" not in self.letter_list:
            letter = input("Введите букву ")
            if letter in self.word:
                self.substitution_letters(letter)
                print(self.letter_list)
            else:
                self.life_point -= 1


game = MainGame()
