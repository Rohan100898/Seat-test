class Seat:
    def __init__(self):
        self.pos = 50

    def fwd(self):
        if self.pos > 0:
            self.pos -= 1

    def bwd(self):
        if self.pos < 100:
            self.pos += 1