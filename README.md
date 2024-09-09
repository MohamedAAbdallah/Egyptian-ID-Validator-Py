# Egyptian ID Validator

**Egyptian ID Validator** is a Python package for validating Egyptian national ID numbers. It ensures that the provided ID meets the required format and checks its validity based on the structure of Egyptian IDs.

## Features

- **Format Validation**: Checks if the ID is in the correct 14-digit format.
- **Checksum Validation**: Verifies the ID using a checksum algorithm.
- **Component Extraction**: Extracts and returns detailed components from the ID, including year, month, day, governorate, and gender.

## Installation

To install the package, you can use pip:

```bash
pip install egyptian-id-validator
```

## Usage

You can use the package directly in your Python code. Here’s an example of how to use the `validate_egyptian_id` function:

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

The project is currently in the **Alpha** stage. Features and functionality may be incomplete, and APIs may change.

## License

This package is licensed under the **CC BY-NC 4.0** License. See the [LICENSE](LICENSE.md) file for more details.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or feature requests, please submit them via GitHub issues or pull requests.

## Author

- **Mohamed A. Abdallah** - [GitHub](https://github.com/MohamedAAbdallah) - eng.mohamed.a.abdallah@gmail.com
