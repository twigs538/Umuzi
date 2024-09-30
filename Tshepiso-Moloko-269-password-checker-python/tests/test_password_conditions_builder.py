from password_checker.password_checker import password_conditions_builder

def test_password_conditions_builder_password_exists() -> None:
    condition = password_conditions_builder("")
    assert condition["password_exists"] == False

def test_password_conditions_builder_password_length() -> None:
    condition = password_conditions_builder("abc123")
    assert condition["password_length"] == False

def test_password_conditions_builder_lowercase() -> None:
    condition = password_conditions_builder("abc123")
    assert condition["lowercase"] == True

def test_password_conditions_builder_uppercase() -> None:
    condition = password_conditions_builder("P@ssw0rd")
    assert condition["uppercase"] == True

def test_password_conditions_builder_digits() -> None:
    condition = password_conditions_builder("P@ssw0rd")
    assert condition["digits"] == True

def test_password_conditions_builder_special_chars() -> None:
    condition = password_conditions_builder("P@ssw0rd")
    assert condition["special_chars"] == True

def test_password_conditions_builder_white_space() -> None:
    condition = password_conditions_builder(" ")
    assert condition["white_space"] == False