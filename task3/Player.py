
class Player:
    def __init__(self, mark):
        self.mark = mark
        self.oposite_mark = self.oposite()
        self.scores = {"X":1, "O":-1, None:0}

    def oposite(self):
        if self.mark == "O":
            return "X"
        elif self.mark == "X":
            return "O"

