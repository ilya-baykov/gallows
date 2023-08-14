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
        letter_list = [len(_word) * ((5 * "\u2014") + "\t")]
        print(*letter_list)
        return letter_list

    @staticmethod
    def substitution_letters(_word, _letter, letter_list):
        for char in range(len(_word)):
            if _word[char] == _letter:
                letter_list[char] = _letter
        return letter_list

    @staticmethod
    def start_game(_word, _letter_list, life_point=LIFE_POINT):
        while life_point > 0:
            letter = input("Введите букву ")
            if letter in _word:
                print("ДА!!!")
            else:
                life_point -= 1


game = MainGame()
word = game.get_random_word()
print(word)

game.start_game(word, game.get_length(word))
