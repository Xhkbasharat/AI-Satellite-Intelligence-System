
# Contributing Guidelines

Thank you for your interest in contributing to the AI Satellite Intelligence System!

Contributions, bug reports, feature suggestions, and documentation improvements are welcome.

## 1. Getting Started

1. Fork this repository.
2. Clone your fork.
3. Create a new branch.
4. Install project dependencies.

```bash
git clone https://github.com/YOUR_USERNAME/AI-Satellite-Intelligence-System.git
cd AI-Satellite-Intelligence-System

python -m venv venv
pip install -r requirements-dev.txt
```

## 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

## 3. Development Guidelines

- Write readable, maintainable Python code.
- Use meaningful variable and function names.
- Follow the existing project structure.
- Add tests for new functionality.
- Document important changes.
- Avoid committing datasets, model weights, credentials, or temporary files.

## 4. Run Tests

Before submitting changes, run:

```bash
pytest -v
```

## 5. Code Formatting

Format Python files using:

```bash
black .
```

Check code quality using:

```bash
flake8 .
```

## 6. Submit a Pull Request

1. Commit your changes.
2. Push your branch.
3. Open a pull request.
4. Explain what changed and why.
5. Include relevant test results.

## 7. Reporting Issues

When reporting a bug, include:

- A clear description.
- Steps to reproduce it.
- Expected behavior.
- Actual behavior.
- Relevant error messages.

Do not upload private satellite imagery or sensitive information in public issues.

## 8. Code of Conduct

Be respectful, constructive, and professional when interacting with contributors.

Thank you for helping improve this project!

---

**Project Author:** Sheikh Basharat Akbar
