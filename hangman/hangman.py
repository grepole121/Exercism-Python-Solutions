# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.orig_word = word
        self.masked_word = len(word) * "_"
        self.list_masked_word = list(self.masked_word)
        self.remaining_guesses = 9

    def guess(self, char):
        self.check_win()

        if char in self.word:
            for i in range(0, self.word.count(char)):
                # Find the position of the character
                pos = self.word.find(char)

                # Remove the underscore from the masked_word at that position
                self.list_masked_word.pop(pos)

                # Add the character to that position
                self.list_masked_word.insert(pos, char)

                # Remove the character from the original word
                self.word = list(self.word)
                self.word.remove(char)
                self.word.insert(pos, " ")
                self.word = "".join(self.word)

                # Update masked_word
                self.masked_word = "".join(self.list_masked_word)
        else:
            if self.remaining_guesses == 0:
                self.status = STATUS_LOSE
                print("You lost")
            self.remaining_guesses -= 1

        if self.masked_word == self.orig_word:
            self.status = STATUS_WIN
            print("You won")
        # Printouts
        print(self.masked_word)
        print(f"Remaining guesses: {self.remaining_guesses}")

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status

    def check_win(self):
        if self.status == STATUS_LOSE:
            raise ValueError("Out of guesses")
        elif self.status == STATUS_WIN:
            raise ValueError("You won")
