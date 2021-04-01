import pytest
import game_of_life
import test


def test_newCellStateTrue():
    assert game_of_life.new_cell_state(game_of_life.first_gen, 1, 3) == "."


def test_newCellStateFalse():
    assert game_of_life.new_cell_state(game_of_life.first_gen, 1, 3) != "x"


@pytest.mark.parametrize("listik, x, y, answer", [(game_of_life.first_gen, 1, 3, "."), (game_of_life.first_gen, 0, 3, ".")])
def test_newCellStateParametrize(listik, x, y, answer):
    assert game_of_life.new_cell_state(listik, x, y) == answer


def test_gameOfLifeOutput():
    test_text = open("test.txt", "r")

    output_list = game_of_life.game_of_life(
        game_of_life.first_gen, game_of_life.gen_num)
    test_text_list = [[j for j in i.rstrip("\n")]
                      for i in test_text.readlines()]
    for x in range(len(output_list)):
        for y in range(len(output_list[x])):
            assert output_list[x][y] == test_text_list[x][y]

    test_text.close()
