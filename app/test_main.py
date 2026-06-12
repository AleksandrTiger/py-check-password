from app.main import check_password


def test_should_return_true_for_valid_password() -> None:
    # Ідеальний стандартний пароль
    assert check_password("Pass@word1") is True


def test_should_return_false_when_password_is_too_short() -> None:
    # Гранична умова: 7 символів (закороткий)
    assert check_password("Pass@12") is False


def test_should_return_true_for_minimum_valid_length() -> None:
    # Гранична умова: рівно 8 символів (мінімальна межа)
    assert check_password("Pass@w12") is True


def test_should_return_true_for_maximum_valid_length() -> None:
    # Гранична умова: рівно 16 символів (максимальна межа)
    assert check_password("Pass@word1234567") is True


def test_should_return_false_when_password_is_too_long() -> None:
    # Гранична умова: 17 символів (задовгий)
    assert check_password("Pass@word12345678") is False


def test_should_return_false_without_uppercase_letters() -> None:
    # Відсутня велика літера
    assert check_password("pass@word1") is False


def test_should_return_false_without_digits() -> None:
    # Відсутня цифра
    assert check_password("Pass@word") is False


def test_should_return_false_without_special_characters() -> None:
    # Відсутній спецсимвол
    assert check_password("Password12") is False


def test_should_return_false_with_invalid_characters() -> None:
    # Використання заборонених символів (% або пробіл)
    assert check_password("Pass%word1") is False
    assert check_password("Pass @word1") is False


def test_should_return_false_with_cyrillic_letters() -> None:
    # Перевірка на не-латинські літери (кирилиця)
    assert check_password("Пасс@word1") is False
