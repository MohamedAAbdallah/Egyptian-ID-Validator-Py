# egyptian_id_validator/validation.py

import re


def validate_id(national_id: str or int) -> dict or None:
    """Validates and extracts details from an Egyptian national ID number.
    
    Args:
        national_id (str or int): The national ID number to validate.

    Returns:
        dict or None: A dictionary containing the extracted components of the ID if valid, None otherwise.
    """

    def __validate_checksum(n_id: str) -> bool:
        w = (2, 7, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 2)
        t = sum(int(d) * w[i] for i, d in enumerate(n_id[:13]))
        k = 11 - t % 11
        k = 0 if k == 10 else (1 if k == 11 else k)
        return k == int(n_id[-1])

    # Ensure the input is a string of digits
    try:
        national_id = str(int(national_id))
    except (ValueError, TypeError):
        return None

    # Check the length of the national ID
    if len(national_id) != 14:
        return None

    if not __validate_checksum(national_id):
        return None

    # Regular expression to extract components from the national ID
    match = re.match(r'^(?P<century>[23])'  # 1st digit: Century (2 or 3)
                     r'(?P<year>\d{2})'  # 2nd and 3rd digits: Year
                     r'(?P<month>0[1-9]|1[0-2])'  # 4th and 5th digits: Month (01-12)
                     r'(?P<day>0[1-9]|[12]\d|3[01])'  # 6th and 7th digits: Day (01-31)
                     r'(?P<governorate>0[1-9]|[1-3]\d|88)'  # 8th and 9th digits: Governorate code
                     r'(?P<unique_number>(?!000)\d{3})'  # 10th to 12th digits: Unique serial number
                     r'(?P<gender>\d)'  # 13th digit: Gender code
                     r'(\d)$',  # 14th digit: Checksum
                     national_id)

    if not match:
        return None

    components = match.groupdict()

    # Calculate the full year based on century code
    year = str(int(components['year']) + (1900 if components['century'] == '2' else 2000))

    # Determine the gender from the gender code
    gender = "M" if int(components['gender']) % 2 else "F"

    try:
        birth_governorate = \
            {1: "Cairo", 2: "Alexandria", 3: "Port Said", 4: "Suez", 11: "Damietta", 12: "Dakahlia", 13: "Sharqia",
             14: "Qalyubia", 15: "Kafr El Sheikh", 16: "Gharbia", 17: "Monufia", 18: "Beheira", 19: "Ismailia",
             21: "Giza", 22: "Beni Suef", 23: "Faiyum", 24: "Minya", 25: "Asyut", 26: "Sohag", 27: "Qena", 28: "Aswan",
             29: "Luxor", 31: "Red Sea", 32: "New Valley", 33: "Matruh", 34: "North Sinai", 35: "South Sinai",
             88: "Foreigners"}[int(components['governorate'])]
    except KeyError:
        return None

    return {
        "Year": year,
        "Month": components['month'],
        "Day": components['day'],
        "Governorate": birth_governorate,
        "Gender": gender
    }
