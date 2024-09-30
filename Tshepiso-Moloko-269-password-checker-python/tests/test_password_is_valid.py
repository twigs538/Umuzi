from password_checker.password_checker import password_is_valid
import pytest

def test_password_is_valid_exist() -> None:
    password = ""
    with pytest.raises(ValueError, match="password should exist"):
        password_is_valid(password)

def test_password_is_valid_length() -> None:
    password = "short"
    with pytest.raises(ValueError, match="password should be longer than 8 characters"):
        password_is_valid(password)

def test_password_is_valid_lowercase() -> None:
    password = "PASSWORD123!"
    with pytest.raises(ValueError, match="password should have at least one lowercase letter"):
        password_is_valid(password)

def test_password_is_valid_uppercase() -> None:
    password = "password123!"
    with pytest.raises(ValueError, match="password should have at least one uppercase letter"):
        password_is_valid(password)

def test_password_is_valid_digit() -> None:
    password = "Password!"
    with pytest.raises(ValueError, match="password should have at least one digit"):
        password_is_valid(password)

def test_password_is_valid_special_character() -> None:
    password = "Password123"
    with pytest.raises(ValueError, match="password should have at least one special character"):
        password_is_valid(password)

def test_password_is_valid_whitespace() -> None:
    password = "Password123!"
    with pytest.raises(ValueError, match="password should have at least one whitespace character"):
        password_is_valid(password)