class HiLo():
    def __init__(self, v=1):
        self.game = v
    def guess(self,n):
        if n < self.game:
            return -1
        if n == self.game:
            return 0
        if n > self.game:
            return 1

# the Hangman game

class Hangman():
    def __init__(self, s="testing"):
        self.word = s
        self.turns = 0
        self.current = len(s) * "_"

    def guess(self, letter):
        pass  # write the code here to make the tests pass