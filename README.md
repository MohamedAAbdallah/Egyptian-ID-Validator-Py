# Egyptian ID Validator

**Egyptian ID Validator** is a Python package designed to validate Egyptian national ID numbers. It ensures the provided ID meets the required format and checks its validity based on the structural rules of Egyptian IDs.

[![ValidationTests](https://github.com/MohamedAAbdallah/Egyptian-ID-Validator-Py/actions/workflows/python-package.yml/badge.svg)](https://github.com/MohamedAAbdallah/Egyptian-ID-Validator-Py/actions/workflows/python-package.yml)

## Features

- **Format Validation**: Ensures the ID is in the correct 14-digit format.
- **Checksum Validation**: Verifies the ID using a checksum algorithm.
- **Component Extraction**: Extracts and returns detailed components from the ID, including:
  - **Year, Month, and Day of Birth**
  - **Governorate of Issue**
  - **Gender**

## Installation

To install the package, run:

```bash
pip install egyptian-id-validator
```

## Usage

Integrate the package in your Python projects with ease. Here’s an example of using the `validate_egyptian_id` function:

```python
from egyptian_id_validator import validate_egyptian_id

id_number = "20001012345678"  # Replace with the ID you want to validate
result = validate_egyptian_id(id_number)

if result:
    print("Valid ID:")
    for key, value in result.items():
        print(f"{key}: {value}")
else:
    print("Invalid ID.")
```

## Development Status

This project is currently in the **Alpha** stage. Features may be incomplete, and APIs are subject to change.

## License

This package is licensed under the **CC BY-NC 4.0** License. See the [LICENSE](LICENSE.md) file for more details.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

For any contributions, please use the GitHub [issues](https://github.com/MohamedAAbdallah/Egyptian-ID-Validator-Py/issues) and [pull requests](https://github.com/MohamedAAbdallah/Egyptian-ID-Validator-Py/pulls) sections.

## Author

- **Mohamed A. Abdallah**  
  - [GitHub Profile](https://github.com/MohamedAAbdallah)  
  - [Email](mailto:eng.mohamed.a.abdallah@gmail.com)

---