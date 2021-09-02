from .hashtable import Hashtable

def test_get_hashtable():
    hashtable = Hashtable()
    hashtable.add("dina", "1234")

    actual = hashtable.find("dina")
    expected = "1234"

    assert actual == expected


def test_contains():

    hashtable = Hashtable()
    hashtable.add('name','dina')
    assert hashtable.contains('name') == True
    assert hashtable.contains('age') == False
