from stack_queue_animal_shelter import __version__
from stack_queue_animal_shelter.stack_queue_animal_shelter import Cat, Node,AnimalShelter,Cat,Dog,Queue


def test_version():
    assert __version__ == '0.1.0'





def test_dequeue_enqueue(shelter_input):
    expected = 'dog1'
    actual = f"{shelter_input.dequeue()}"
    assert actual == expected


def test_dequeue_dog_or_cat():
    shelter= AnimalShelter()
    expected = "Null"
    actual= f"{shelter.dequeue('cat')}"
    assert actual == expected
