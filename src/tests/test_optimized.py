from algorithms.optimized import dynamic_programming


def test_dynamic_programming():
    assert dynamic_programming(7, [5, 3, 1, 4], [100, 55, 18, 70]) == [2, 4]
    assert dynamic_programming(15, [2, 5, 7, 12, 9], [1, 2, 3, 7, 10]) == [2, 5]
    assert dynamic_programming(12, [1, 2, 5, 6, 7], [1, 6, 18, 22, 24]) == [3, 5]
    assert dynamic_programming(10, [2, 3, 4, 4, 8], [3, 5, 6, 7, 10]) == [1, 3, 4]
