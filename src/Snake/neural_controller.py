from src.Snake.MiniSnake import play

MOVE_VECTORS = {
    'left': (-1, 0),
    'right': (1, 0),
    'up': (0, -1),
    'down': (0, 1)
}

ADJACENT_VECTORS = {
    'left': ('left', 'down', 'up'),
    'up': ('up', 'left', 'right'),
    'right': ('right', 'up', 'down'),
    'down': ('down', 'right', 'left')
}


class NeuralController:
    def __init__(self, neural_network):
        self.nn = neural_network

    def feed(self, **kw):

        def scan_segments(segments, pos):
            for segment in segments:
                if segment.tilepos == pos:
                    return segment
            return None

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

        directions_to_scan = ADJACENT_VECTORS[head_direction]

        # scan directions
        objects_ahead = []
        for direction in directions_to_scan:
            scan_point = (head_position[0] + MOVE_VECTORS[direction][0], head_position[1] + MOVE_VECTORS[direction][1])
            distance = 1
            while 0 <= scan_point[0] <= board_size[0] and 0 <= scan_point[1] <= board_size[1]:
                try:
                    if int(apple.rect.topleft[0] / tile_size[0]) == scan_point[0] and \
                            int(apple.rect.topleft[1] / tile_size[1]) == scan_point[1]:
                        objects_ahead.append(1)  # apple ahead
                        break
                except AttributeError:
                    pass

                if scan_segments(segments, scan_point):
                    objects_ahead.append(2)
                    break

                scan_point = (
                    scan_point[0] + MOVE_VECTORS[direction][0],
                    scan_point[1] + MOVE_VECTORS[direction][1]
                )
                distance += 1
            else:
                objects_ahead.append(0)  # nothing ahead
            objects_ahead.append(distance)

        # normalize flags
        for i in range(0, len(objects_ahead), 2):
            objects_ahead[i] /= 2
        # normalize distances
        for i in range(1, len(objects_ahead), 2):
            objects_ahead[i] /= max(board_size)

        nn_output = self.nn.feed(objects_ahead)

        # TODO apply output to game (press key...?)

        max_index = nn_output.index(max(nn_output))

        # 0 -> go forward (do nothing)
        # 1 -> turn left
        # 2 -> turn right
        snek.movedir = ADJACENT_VECTORS[snek.movedir][max_index]


def fit(candidate, **kwargs):
    controller = NeuralController(candidate)
    score = play(controller)
    return score
