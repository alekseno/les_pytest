import pytest

@pytest.fixture()
def set_up():
    print("\n\n---Вход в систему---\n") # действия до начала теста
    yield
    print("\n---------------------Выход из системы------") #Действия после теста


@pytest.fixture(scope="module") #scope="cls", "function"
def some():
    print("\n\n----Начало работы программы----\n")
    yield
    print("\n-----------------Завершение работы программы----")