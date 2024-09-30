import pytest
from validate_sa_id.validate_sa_id import is_id_number_valid, is_valid_citizenship, is_valid_date, is_valid_checksum_digit, is_valid_gender

def test_is_id_number_valid_empty():
    assert is_id_number_valid('') == False

def test_is_id_number_valid_invalid_id():
    assert is_id_number_valid('9209224994086') == False

def test_is_id_number_valid_valid_id():
    assert is_id_number_valid('8109201095081') == True

def test_is_id_number_valid_short():
    assert is_id_number_valid('456') == False

def test_is_id_number_valid_long():
    assert is_id_number_valid('1234567891011121314151617181920') == False

def test_non_digit_in_id_number():
    assert is_id_number_valid('20010A4800086') == False

def test_is_id_number_valid_invalid_year():
    assert is_id_number_valid('3009201095081') == False

def test_is_id_number_valid_invalid_month():
    assert is_id_number_valid('8120201095081') == False

def test_is_id_number_valid_invalid_day():
    assert is_id_number_valid('8109991095081') == False

def test_is_id_number_valid_invalid_citizen():
    assert is_id_number_valid('8109201095581') == False

def test_is_valid_date_true():
    assert is_valid_date('200101') == True

def test_is_valid_date_false():
    assert is_valid_date('210230') == False

def test_is_valid_gender_true():
    assert is_valid_gender('0000') == True

def test_is_valid_gender_false():
    assert is_valid_gender('10000') == False

def test_is_valid_citizenship_true():
    assert is_valid_citizenship('0') == True

def test_is_valid_citizenship_false():
    assert is_valid_citizenship('2') == False

def test_is_valid_checksum_digit_true():
    assert is_valid_checksum_digit('2001014800086') == True

def test_is_valid_checksum_digit_false():
    assert is_valid_checksum_digit('2001014800087') == False