from person.person import Person

def test_interests_empty() -> None:
    person = Person('Ryan', 30, 'male', [])
    greeting = person.hello()
    assert greeting == "Hello, my name is Ryan, my gender is male and I am 30 years old. I have no interests."

def test_interests_single_item() -> None:
    person = Person('Ryan', 30, 'male', ['being a hardarse'])
    greeting = person.hello()
    assert greeting == "Hello, my name is Ryan, my gender is male and I am 30 years old. My interest is being a hardarse."

def test_interests_multiple_items() -> None:
    person = Person('Ryan', 30, 'male', ['reading','coding'])
    greeting = person.hello()
    assert greeting == "Hello, my name is Ryan, my gender is male and I am 30 years old. My interests are reading and coding."