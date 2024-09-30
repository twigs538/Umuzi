from simple_calculator.calculator import add, multiply

def test_add_empty() -> None:
    assert add() == 0

def test_add_positve_single_item() -> None:
    assert add(4) == 4

def test_add_negative_single_item() -> None:
    assert add(-3) == -3

def test_add_three_positve_multiple_items() -> None:
    assert add(4,5,6) == 15

def test_add_three_negative_multiple_items() -> None:
    assert add(-1,-2,-3) == -6

def test_add_two_positive_and_one_negative_mutiple_items() -> None:
    assert add(-5,5,1) == 1

def test_multiply_empty() -> None:
    assert multiply() == 0

def test_multiply_positve_single_item() -> None:
    assert multiply(5) == 5

def test_multiply_negative_single_item() -> None:
    assert multiply(-7) == -7

def test_multiply_three_positve_multiple_items() -> None:
    assert multiply(2,4,5) == 40

def test_multiply_two_negative_multiple_items() -> None:
    assert multiply(-6,-2) == 12

def test_multiply_one_positve_and_one_negative_multiple_items() -> None:
    assert multiply(-5,5) == -25

def test_add_four_postive_and_one_negative_numbers_multiple_items() -> None:
    assert add(2,4,5,-10,36) == 37

def test_multip_two_postive_and_five_negative_numbers() -> None:
    assert multiply(2,4,-6,-8,-10,-12,-14) == -645120