class NeuralController:
    def __init__(self, neural_network):
        self.nn = neural_network

    def feed(self, **kw):
        try:
            board_size = kw['board_size']
            snek = kw['snek']
            apple = kw['apple']
        except KeyError:
            raise RuntimeError
        # TODO build nn input
        head_position = snek.tilepos
        head_direction = snek.movedir
        # nn_output = self.nn.feed(something)

        # TODO apply output to game (press key...?)
