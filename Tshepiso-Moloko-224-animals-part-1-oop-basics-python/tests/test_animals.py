import pytest
from animals.animals import Animal, Dog, Cat, Home


@pytest.fixture
def animal_instance():
    return Animal("Generic animal")


@pytest.fixture
def dog_instance_default():
    return Dog()


@pytest.fixture
def cat_instance_default():
    return Cat()


@pytest.fixture
def dog_instance():
    return Dog("Gent")


@pytest.fixture
def cat_instance():
    return Cat("Furry")


@pytest.fixture
def home():
    return Home()


def test_dog_instance_default_name(dog_instance_default):
    assert dog_instance_default.name == "Rax"


def test_cat_instance_default_name(cat_instance_default):
    assert cat_instance_default.name == "Stormy"


def test_dog_instance_name(dog_instance):
    assert dog_instance.name == "Gent"


def test_cat_instance_name(cat_instance):
    assert cat_instance.name == "Furry"


def test_animal_instance_name(animal_instance):
    assert animal_instance.name == "Generic animal"


def test_dog_instance_sound(dog_instance):
    assert dog_instance.sound() == "Bark"


def test_cat_instance_sound(cat_instance):
    assert cat_instance.sound() == "Meow"


def test_animal_instance_sound(animal_instance):
    assert animal_instance.sound() == "sound..."


def test_dog_instance_default_eat(dog_instance_default):
    assert dog_instance_default.eat() == "Rax eats"


def test_cat_instance_default_eat(cat_instance_default):
    assert cat_instance_default.eat() == "Stormy eats"


def test_dog_instance_eat(dog_instance):
    assert dog_instance.eat() == "Gent eats"


def test_cat_instance_eat(cat_instance):
    assert cat_instance.eat() == "Furry eats"


def test_animal_instance_eat(animal_instance):
    assert animal_instance.eat() == "Generic animal eats"


def test_dog_instance_adopt_pet_ok(home, dog_instance):
    assert home.adopt_pet(dog_instance) == 1


def test_cat_instance_adopt_pet_ok(home, cat_instance):
    assert home.adopt_pet(cat_instance) == 1


def test_adopt_pet_error(home, dog_instance):
    home.adopt_pet(dog_instance)
    with pytest.raises(ValueError, match="Cannot adopt the same pet twice!"):
        home.adopt_pet(dog_instance)


def test_dog_instance_inheritance():
    assert issubclass(Dog, Animal)


def test_cat_instance_inheritance():
    assert issubclass(Cat, Animal)


@pytest.mark.parametrize("sounds", [["Bark", "Meow"]])
def test_make_all_sounds(home, sounds, dog_instance, cat_instance):
    if sounds:
        home.adopt_pet(dog_instance)
        home.adopt_pet(cat_instance)
    assert home.make_all_sounds() == sounds
