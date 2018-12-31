from src.Snake.MiniSnake import play

class Dummy:
    def feed(self, **kw):
        print(kw)


print(play(Dummy()))