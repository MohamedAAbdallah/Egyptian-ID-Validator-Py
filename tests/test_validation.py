# tests/test_validation.py

import pytest
from egyptian_id_validator.validation import validate_egyptian_id

def test_valid_id():
    valid_id = "30012240199937"
    result = validate_egyptian_id(valid_id)
    assert result is not None
    assert result["Year"] == "2000"
    assert result["Month"] == "12"
    assert result["Day"] == "24"
    assert result["Governorate"] == "Cairo"
    assert result["Gender"] == "M"

def test_invalid_id_empty():
    invalid_id = ""
    result = validate_egyptian_id(invalid_id)
    assert result is None

def test_invalid_id_wrong_type():
    invalid_id = [30012240199937]
    result = validate_egyptian_id(invalid_id)
    assert result is None

def test_invalid_id_short():
    invalid_id = "3001224019993"  # Too short
    result = validate_egyptian_id(invalid_id)
    assert result is None

def test_invalid_id_long():
    invalid_id = "300122401999371"  # Too long
    result = validate_egyptian_id(invalid_id)
    assert result is None

def test_invalid_id_format():
    invalid_id = "3001224019X930"
    result = validate_egyptian_id(invalid_id)
    assert result is None

def test_invalid_id_checksum():
    invalid_id = "30012240199930"  # Wrong checksum
    result = validate_egyptian_id(invalid_id)
    assert result is None
    
def test_invalid_id_century():    
    invalid_ids = ["00012240199930", "10012240199939", "40012240199936"]  # Invalid century
    for id in invalid_ids:
        result = validate_egyptian_id(id)
        assert result is None

def test_invalid_id_month():
    invalid_ids = ["30000240199930", "30013240199936", "30099240199932"]  # Invalid month
    for id in invalid_ids:
        result = validate_egyptian_id(id)
        assert result is None

def test_invalid_id_governorate():
    invalid_id = "30012249999930"  # Invalid governorate code
    result = validate_egyptian_id(invalid_id)
    assert result is None
    
def test_invalid_id_unique_number():
    invalid_id = "30012240000035"  # Invalid unique number
    result = validate_egyptian_id(invalid_id)
    assert result is None

def test_valid_id_male():
    valid_id = "30012240199937"  # Example ID for a male
    result = validate_egyptian_id(valid_id)
    assert result is not None
    assert result["Gender"] == "M"

def test_valid_id_female():
    valid_id = "30012240199946"  # Example ID for a female
    result = validate_egyptian_id(valid_id)
    assert result is not None
    assert result["Gender"] == "F"

if __name__ == "__main__":
    pytest.main()
