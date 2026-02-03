# DeepBreathe

<p align="center">
  <img src="deepbreathe/assets/images/logo.svg" alt="DeepBreathe Logo" width="200">
</p>

A cross-platform apnea and breath-holding training app built with Python and Kivy.

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Python Kivy](https://img.shields.io/badge/Python-Kivy-555555?logo=python&logoColor=white&labelColor=555555&color=8b5cf6)](https://kivy.org/)

## Features

- **O2 Tables** - Fixed hold time with decreasing rest periods to improve oxygen efficiency
- **CO2 Tables** - Increasing hold time with fixed rest periods to build CO2 tolerance
- **Free Training** - Practice breath holds at your own pace with a simple timer
- **Customizable Settings** - Adjust hold times, rest periods, and number of rounds
- **Visual Progress** - Animated progress circle with phase-based color feedback

## Development

### Setup

```bash
# Install development dependencies
uv sync --extra dev

# Install pre-commit hooks
uv run pre-commit install
```

### Running in Development Mode

Development mode stores the database in the project directory instead of the system data directory:

```bash
uv run --env-file .env.development deepbreathe
```

Or set the environment variable manually:

```bash
DEEPBREATHE_DEV=1 uv run deepbreathe
```

### Code quality

```bash
uv run ruff check .
```

```
uv run ruff format .
```

