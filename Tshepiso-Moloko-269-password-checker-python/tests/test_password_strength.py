from password_checker.password_checker import password_strength

def test_password_strength_strong() -> None:
    assert password_strength("StrongP@ssw0rd!") == "strong"

def test_password_strength_medium() -> None:
    assert password_strength("MediumP@ss") == "medium"

def test_password_strength_invalid_length() -> None:
    assert password_strength("P@ssw 12") == "invalid"

def test_password_strength_invalid_existence() -> None:
    assert password_strength("") == "invalid"

def test_password_strength_invalid_criteria() -> None:
    assert password_strength("shortpa") == "invalid"

def test_password_strength_empty_password() -> None:
    assert password_strength("") == "invalid"