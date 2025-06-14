# Contributing to Egyptian ID Validator (Python)

First off, thank you for your interest in contributing to this project!  
Whether you're here to report a bug, suggest a feature, or contribute code. Your input is appreciated.

---

## 📌 Before You Begin

- This repository is part of a larger project under [Egyptian-ID-Validator](https://github.com/MohamedAAbdallah/Egyptian-ID-Validator).
- The Python version is stable and released on [PyPI](https://pypi.org/project/egyptian-id-validator/).
- All validation logic follows the official Egyptian ID structure, including a private checksum algorithm. **Please do not attempt to reverse engineer or disclose it.**.

---

## ✅ Ways to Contribute

### 🔧 Report Bugs
- Use the [GitHub Issues](https://github.com/MohamedAAbdallah/Egyptian-ID-Validator-Py/issues) section.
- Include a clear title, reproduction steps, expected vs actual behavior, and sample ID if applicable.

### 💡 Suggest Features
- Keep suggestions focused on developer use cases.
- If your idea is for external interfaces (e.g., web API, GUI), consider submitting it to the [mother repo](https://github.com/MohamedAAbdallah/Egyptian-ID-Validator).

### 🧪 Submit Code
- Fork the repo
- Create a new branch: `git checkout -b feature/your-feature-name`
- Commit changes: `git commit -m "Add your message here"`
- Push to your fork: `git push origin feature/your-feature-name`
- Open a pull request against `main`

---

## 🧼 Code Standards

- Python 3.8+
- Follow [PEP8](https://peps.python.org/pep-0008/)
- Lint using `flake8`
- Test using `pytest`
- Use `PYTHONPATH=src` when running tests locally

---

## 📦 Versioning & Releases

- All code changes must include a **version bump** in `pyproject.toml`
- Version bumps are enforced via GitHub Actions
- Only maintainers push to `main`; all changes go through pull requests

---

## 🔐 License and Respect

By contributing, you agree to license your code under the [CC BY-NC 4.0 License](LICENSE.md) and respect the project’s **non-commercial scope**.

---

Thank you again for your support and contributions!

- Mohamed A. Abdallah  
[GitHub](https://github.com/MohamedAAbdallah)
