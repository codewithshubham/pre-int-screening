import pytest
from functions.word_count_sorted import check_word_count  

def test_empty_string():
    assert check_word_count("") == {}

def test_single_word():
    assert check_word_count("Word") == {"word": 1}

def test_multiple_same_words():
    assert check_word_count("word word word") == {"word": 3}

def test_different_words():
    assert check_word_count("This is a test") == {"a": 1, "is": 1, "test": 1, "this": 1}

def test_mixed_case():
    assert check_word_count("Python python PyThOn") == {"python": 3}

def test_special_characters():
    assert check_word_count("Hello, hello!") == {"hello,": 1, "hello!": 1}

def test_extra_spaces():
    assert check_word_count("This  is  a    test") == {"a": 1, "is": 1, "test": 1, "this": 1}

def test_numbers_as_words():
    assert check_word_count("1 2 3 1") == {"1": 2, "2": 1, "3": 1}

def test_case_insensitivity_with_numbers():
    assert check_word_count("Python 2 Python 3 python 2") == {"2": 2, "3": 1, "python": 3}