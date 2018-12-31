from src.Snake.MiniSnake import play

MOVE_VECTORS = {
    'left': (-1, 0),
    'right': (1, 0),
    'up': (0, -1),
    'down': (0, 1)
}

ADJACENT_VECTORS = {
    'left': ('down', 'up'),
    'up': ('left', 'up'),
    'right': ('up', 'down'),
    'down': ('right', 'left')
}


class NeuralController:
    def __init__(self, neural_network):
        self.nn = neural_network

    def feed(self, **kw):
        try:
            board_size = kw['board_size']
            snek = kw['snek']
            apple = kw['apple']
            tile_size = kw['tile_size']

        except KeyError:
            raise RuntimeError
        # TODO build nn input
        head_position = snek.tilepos
        head_direction = snek.movedir

        # segments to list
        segments = []
        segment = snek.behind_segment
        while segment.behind_segment is not None:
            segment = segment.behind_segment
            segments.append(segment)

        directions_to_scan = (head_direction, ADJACENT_VECTORS[head_direction][0], ADJACENT_VECTORS[head_direction][1])

        objects_ahead = []
        for direction in directions_to_scan:
            scan_point = (head_position[0] + MOVE_VECTORS[direction][0], head_position[1] + MOVE_VECTORS[direction][1])
            distance = 1
            while 0 <= scan_point[0] * tile_size[0] < board_size[0] and 0 <= scan_point[1] * tile_size[1] < board_size[
                1]:
                try:
                    if apple.tilepos == scan_point:
                        objects_ahead.append(1)  # apple ahead
                        break
                except AttributeError:
                    pass
                for segment in segments:
                    if segment.tilepos == scan_point:
                        objects_ahead.append(2)  # tail_ahead
                        objects_ahead.append(distance)
                        break
                scan_point = (
                    scan_point[0] + MOVE_VECTORS[direction][0],
                    scan_point[1] + MOVE_VECTORS[direction][1]
                )
                distance += 1
            else:
                objects_ahead.append(0)  # nothing ahead
            objects_ahead.append(distance)

        nn_output = self.nn.feed(objects_ahead)

        # TODO apply output to game (press key...?)


def fit(candidate, **kwargs):
    controller = NeuralController(candidate)
    score = play(controller)
    return score
