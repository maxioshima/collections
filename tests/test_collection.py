import pytest
from Collection.collection import unique_characters_counter

class UniqueCharactersTests:
    def test_of_expected_value1(self):
        assert unique_characters_counter('aab34t') == 4


    def test_of_expected_value2(self):
        assert unique_characters_counter('1123455') == 3


    def test_one_more_word(self):
        assert unique_characters_counter('abcc12 23nn 11l') == 4


    def test_of_type_1(self):
        with  pytest.raises(TypeError):
            unique_characters_counter(1)


    def test_of_type_2(self):
        with  pytest.raises(TypeError):
            unique_characters_counter(print())


    def test_of_type_3(self):
        with  pytest.raises(TypeError):
            unique_characters_counter(True)
