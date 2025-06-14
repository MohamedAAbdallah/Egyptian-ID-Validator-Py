import pytest

from egyptian_id_validator import validate_id


# Invalid format cases
@pytest.mark.parametrize("invalid_id", ["",  # Empty string
                                        "abc",  # Non-numeric
                                        "3001224019993",  # Too short
                                        "300122401999371",  # Too long
                                        "3001224019X930",  # Contains invalid character
                                        [30012240199937],  # Wrong type
                                        None,  # None input
                                        ])
def test_invalid_formats(invalid_id):
    assert validate_id(invalid_id) is None


# Invalid checksum
def test_invalid_checksum():
    assert validate_id("30012240199930") is None


# Invalid century digit
@pytest.mark.parametrize("nid", ["00012240199930", "10012240199939", "40012240199936"])
def test_invalid_century(nid):
    assert validate_id(nid) is None


# Invalid months
@pytest.mark.parametrize("nid", ["30000240199930",  # Month 00
                                 "30013240199936",  # Month 13
                                 "30099240199932",  # Month 99
                                 ])
def test_invalid_months(nid):
    assert validate_id(nid) is None


# Invalid days
@pytest.mark.parametrize("nid", ["30001320199935"  # Day 00
                                 ])
def test_invalid_days(nid):
    assert validate_id(nid) is None


# Invalid governorate
def test_invalid_governorate():
    assert validate_id("30012249999930") is None


# Invalid unique number
def test_invalid_unique_number():
    assert validate_id("30012240000035") is None
