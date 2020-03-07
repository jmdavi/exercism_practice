import string

# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.phrase = word.lower()
        # start with all letters masked as underscores '_', remove letters from list to unmask as themselves
        self.mask_letters = string.ascii_lowercase

    def guess(self, char):
        """Accept player guess of letter, iterate remaining_guesses down by 1, take out of guessing pool mask_letters"""
        # remove player's guess from letters to mask
        if self.status != STATUS_ONGOING:
            raise ValueError("The game isn't active anymore")
        if char.lower() not in self.phrase or char.lower() not in self.mask_letters:
            self.remaining_guesses += -1
        self.mask_letters = self.mask_letters.replace(char.lower(), '')
        self.get_status()

    def get_masked_word(self):
        """Any letters contained within mask_letters will be displayed to user as underscores"""
        transtable = ''.maketrans(self.mask_letters, '_' * len(self.mask_letters), '')
        return self.phrase.translate(transtable)

    def get_status(self):
        masked_word = self.get_masked_word()
        print(self.status, self.remaining_guesses)
        print(masked_word, self.phrase, self.mask_letters)
        if self.phrase == masked_word:
            self.status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        else:
            self.status = STATUS_ONGOING
        return self.status
