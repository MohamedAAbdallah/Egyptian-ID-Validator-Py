# Egyptian ID Validator (Python)

[![PyPI version](https://img.shields.io/pypi/v/egyptian-id-validator.svg)](https://pypi.org/project/egyptian-id-validator/)
[![Python Versions](https://img.shields.io/pypi/pyversions/egyptian-id-validator)](https://pypi.org/project/egyptian-id-validator/)
[![Build](https://github.com/MohamedAAbdallah/Egyptian-ID-Validator-Py/actions/workflows/python-package.yml/badge.svg)](https://github.com/MohamedAAbdallah/Egyptian-ID-Validator-Py/actions/workflows/python-package.yml)
[![License](https://img.shields.io/badge/license-MIT--Custom-blue)](LICENSE.md)

---

**Egyptian ID Validator** is a production-ready Python package for validating and parsing Egyptian national ID numbers.  
It enforces the official structural rules defined by the Egyptian Ministry of Interior, including a verified but undisclosed checksum mechanism.

> ℹ️ This package is part of a broader multi-language validation system.  
> For other implementations (e.g., Java, NPM), see the [Egyptian-ID-Validator](https://github.com/MohamedAAbdallah/Egyptian-ID-Validator) mother repository.

---

## 🔍 Features

- ✅ **Format Validation** – Ensures the ID is 14 digits and correctly structured.
- ✅ **Checksum Validation** – Verifies integrity using an official checksum method.
- ✅ **Component Extraction** – Parses the ID into:
  - Year, Month, and Day of Birth
  - Governorate Name and Code
  - Gender (Male/Female)

---

## 📦 Installation

Install directly from PyPI:

```bash
pip install egyptian-id-validator
````

>Supports Python >3.8.

---

## 🚀 Quick Usage

```python
from egyptian_id_validator.validation import validate_egyptian_id

id_number = "20001012345678"  # Replace with the ID you want to validate
result = validate_egyptian_id(id_number)

if result:
    print("Valid ID:")
    for key, value in result.items():
        print(f"{key}: {value}")
else:
    print("Invalid ID.")
```

---

## 📁 Project Status

This package is **stable** and currently in **production** use.
All validation logic adheres to official specifications.

---

## 🤝 Contributing

Contributions are welcome — especially for:
* Bug reports
* Feature suggestions
* Language porting alignment

Please use [Issues](https://github.com/MohamedAAbdallah/Egyptian-ID-Validator-Py/issues) and [Pull Requests](https://github.com/MohamedAAbdallah/Egyptian-ID-Validator-Py/pulls).

---

## 📄 License

This project is licensed under a custom [MIT License with Limited Commercial Use Restrictions](LICENSE.md).

You are free to use, modify, and integrate the package — including in commercial projects — **as long as**:
- You provide proper attribution
- You do **not** sell, sublicense, or rely on this package as the **core functionality** or **main value** of a monetized product or service without prior permission

See the [LICENSE.md](LICENSE.md) file for full terms.

---

## 👤 Author

**Mohamed A. Abdallah**

[GitHub](https://github.com/MohamedAAbdallah) | [Email](mailto:eng.mohamed.a.abdallah@gmail.com)
