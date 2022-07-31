def snail(array):
    if array == [[]]:
        return []

    x_min = 0
    x_max = len(array[0]) - 1
    y_min = 0
    y_max = len(array) - 1

    result = [array[0][0]]

    def append_move(move, y, x, limit):
        for i in move(y, x, limit):
            yi, xi = i
            result.append(array[yi][xi])

    append_move(move_right, y_min, x_min + 1, x_max)
    while True:
        y_min += 1

        if not needs_move(y_min, y_max):
            break
        append_move(move_down, y_min, x_max, y_max)
        x_max -= 1

        if not needs_move(x_min, x_max):
            break
        append_move(move_left, y_max, x_max, x_min)
        y_max -= 1

        if not needs_move(y_min, y_max):
            break
        append_move(move_up, y_max, x_min, y_min)
        x_min += 1

        if not needs_move(x_min, x_max):
            break
        append_move(move_right, y_min, x_min, x_max)

    return result


def needs_move(lo, hi):
    return lo <= hi


def move_right(y, x, x_max):
    return ((y, xi) for xi in range(x, x_max + 1))


def move_down(y, x, y_max):
    return ((yi, x) for yi in range(y, y_max + 1))


def move_left(y, x, x_min):
    return ((y, xi) for xi in reversed(range(x_min, x + 1)))


def move_up(y, x, y_min):
    return ((yi, x) for yi in reversed(range(y_min, y + 1)))
