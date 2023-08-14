from random import choice

from fiile_preparation import FileEditor


class MainGame(FileEditor):
    LIFE_POINT = 7

    @classmethod
    def get_random_word(cls):
        random_word = cls.read_file("Words_raw")
        return choice(random_word)

    @staticmethod
    def get_length(_word: str):
        print(len(_word) * ((5 * "\u2014") + "\t"))

    def start_game(self):
        pass


game = MainGame()
word = game.get_random_word()
print(word)
game.get_length(word)
print(game)
