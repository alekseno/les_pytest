import pytest

@pytest.mark.run(order=2)
def test_method_1():
    print("\nМетод 1\n")

@pytest.mark.run(order=1)
def test_method_2():
    print("\nМетод 2\n")

@pytest.mark.run(order=5)
def test_method_3():
    print("\nМетод 3\n")

@pytest.mark.run(order=4)
def test_method_4():
    print("\nМетод 4\n")

@pytest.mark.run(order=6)
def test_method_5():
    print("\nМетод 5\n")

@pytest.mark.run(order=3)
def test_method_5():
    print("\nМетод 6\n")