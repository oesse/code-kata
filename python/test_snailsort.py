from snailsort import snail


# def test_foo():
#     print([x for x in move_right(0, 0, 3)])
#     print([x for x in move_down(0, 3, 3)])
#     print([x for x in move_left(3, 3, 0)])
#     print([x for x in move_up(3, 0, 0)])



def test_snail_0x0():
    array = [[]]
    assert [] == snail(array)


def test_snail_1x1():
    array = [[1]]
    assert [1] == snail(array)


def test_snail_2x2():
    array = [[1, 2],
             [3, 4]]
    assert [1, 2, 4, 3] == snail(array)


def test_snail_3x3():
    array = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    assert [1, 2, 3, 6, 9, 8, 7, 4, 5] == snail(array)


def test_snail_4x4():
    array = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
    assert [1, 2, 3, 4, 8, 12, 16, 15,
            14, 13, 9, 5, 6, 7, 11, 10] == snail(array)
