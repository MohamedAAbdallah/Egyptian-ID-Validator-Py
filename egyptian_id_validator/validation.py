# egyptian_id_validator/validation.py

import re


def validate_egyptian_id(national_id: str):
    """Validates and extracts details from an Egyptian national ID number.
    
    Args:
        national_id (str): The national ID number to validate.

    Returns:
        dict or None: A dictionary containing the extracted components of the ID if valid, None otherwise.
    """
    # Ensure the input is a string of digits
    try:
        national_id = str(int(national_id))
    except ValueError:
        return None

    # Check the length and the checksum of the national ID
    if len(national_id) != 14 or 10 - (sum(int(d) for d in national_id[:-1]) % 10) != int(national_id[-1]):
        return None

    # Regular expression to extract components from the national ID
    match = re.match(
        r'^(?P<century>[23])'  # 1st digit: Century (2 or 3)
        r'(?P<year>\d{2})'  # 2nd and 3rd digits: Year
        r'(?P<month>0[1-9]|1[0-2])'  # 4th and 5th digits: Month (01-12)
        r'(?P<day>0[1-9]|[12]\d|3[01])'  # 6th and 7th digits: Day (01-31)
        r'(?P<governorate>0[1-9]|1\d|2[0-9])'  # 8th and 9th digits: Governorate code
        r'(?P<unique_number>[0-9]{3})'  # 10th to 12th digits: Unique serial number
        r'(?P<gender>[1-9])'  # 13th digit: Gender code
        r'(\d)$',  # 14th digit: Checksum
        national_id
    )

    if not match:
        return None

    components = match.groupdict()

    # Calculate the full year based on century code
    year = str(int(components['year']) + (1900 if components['century'] == '2' else 2000))

    # Determine the gender from the gender code
    gender = "M" if int(components['gender']) % 2 else "F"

    # Map the governorate code to the governorate name
    birth_governorate = {
        1: "Cairo", 2: "Alexandria", 3: "Port Said", 4: "Suez", 11: "Damietta", 12: "Dakahlia", 13: "Sharqia",
        14: "Qalyubia", 15: "Kafr El Sheikh", 16: "Gharbia", 17: "Monufia", 18: "Beheira", 19: "Ismailia", 21: "Giza",
        22: "Beni Suef", 23: "Faiyum", 24: "Minya", 25: "Asyut", 26: "Sohag", 27: "Qena", 28: "Aswan", 29: "Luxor",
        31: "Red Sea", 32: "New Valley", 33: "Matruh", 34: "North Sinai", 35: "South Sinai", 88: "Foreigners"
    }.get(int(components['governorate']), 'Unknown')

    # Return the extracted information as a dictionary
    return {
        "Year": year,
        "Month": components['month'],
        "Day": components['day'],
        "Governorate": birth_governorate,
        "Gender": gender
    }
