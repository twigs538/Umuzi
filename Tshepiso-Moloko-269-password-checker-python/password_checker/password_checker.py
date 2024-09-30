import re

def password_is_valid(password):
    password_conditions_dict = password_conditions_builder(password)
    conditions = [
        (password_conditions_dict["password_exists"], "password should exist"),
        (
            password_conditions_dict["password_length"],
            "password should be longer than 8 characters",
        ),
        (
            password_conditions_dict["lowercase"],
            "password should have at least one lowercase letter",
        ),
        (
            password_conditions_dict["uppercase"],
            "password should have at least one uppercase letter",
        ),
        (password_conditions_dict["digits"], "password should have at least one digit"),
        (
            password_conditions_dict["special_chars"],
            "password should have at least one special character",
        ),
        (
            password_conditions_dict["white_space"],
            "password should have at least one whitespace character",
        ),
    ]

    for condition, error_message in conditions:
        if not condition or condition is None:
            raise ValueError(error_message)

    return True

def password_strength(password):
    password_conditions_dict = password_conditions_builder(password)
    conditions_met = len(
        [condition for condition in password_conditions_dict.values() if condition]
    )

    if (
        not password_conditions_dict["password_exists"]
        or not password_conditions_dict["password_length"]
    ):
        return "invalid"
    if conditions_met >= 6:
        return "strong"
    elif conditions_met >= 4:
        return "medium"
    elif conditions_met == 3:
        return "weak"

def password_conditions_builder(password):
    return {
        "password_exists": len(password) > 0,
        "password_length": len(password) > 8,
        "lowercase": re.search("[a-z]", password),
        "uppercase": re.search("[A-Z]", password),
        "digits": re.search("[0-9]", password),
        "special_chars": re.search(r"[^\sa-zA-Z0-9]+", password),
        "white_space": re.search(r"[\s]", password)
    }

if __name__ == "__main__":
    print(password_is_valid("#Takeoff 123"))