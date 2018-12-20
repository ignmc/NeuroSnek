import random


class Individual:
    def __init__(self, size, vocabulary):
        # maybe not every individual should know the vocabulary for its genes
        self.vocabulary = vocabulary
        self.sequence = [None] * size
        self.size = size

    def __str__(self):
        return "Individual with genes {}".format(str(self.sequence))

    def __repr__(self):
        return "Individual with genes {}".format(str(self.sequence))

    def randomize(self):
        for i in range(self.size):
            self.sequence[i] = random.choice(self.vocabulary)
