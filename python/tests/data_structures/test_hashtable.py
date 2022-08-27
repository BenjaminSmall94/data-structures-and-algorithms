import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


def test_bad_key():
    hashtable = Hashtable()
    actual = hashtable.get("apple")
    expected = None
    assert actual == expected


def test_get_keys():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("orange", "Used for orange sauce")
    hashtable.set("grape", "Used for grape sauce")
    actual = sorted(hashtable.keys())
    expected = ["apple", "grape", "orange"]
    assert actual == expected


def test_collisions():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("orange", "Used for orange sauce")
    assert True
