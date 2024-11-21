[![Tests](https://github.com/leon-gorissen/pritty_logger/actions/workflows/test.yml/badge.svg)](https://github.com/leon-gorissen/pritty_logger/actions/workflows/test.yml)
[![Build](https://github.com/leon-gorissen/pritty_logger/actions/workflows/build.yml/badge.svg)](https://github.com/leon-gorissen/pritty_logger/actions/workflows/build.yml)
[![Python package](https://github.com/leon-gorissen/pritty_logger/actions/workflows/publish.yml/badge.svg)](https://github.com/leon-gorissen/pritty_logger/actions/workflows/publish.yml)

# Pritty logger

A simple logger that logs to console using the rich library and to file in /var/log/ or to ~/.log/. Created to simplify setting up logging in containerized development and deployment.

## Installation 

```bash
pip install pritty_logger
``` 

## Usage

```python
from pritty_logger import RichLogger

logger = RichLogger("example")
logger.log("This is an info message")
logger.log({"key": "value"}, level="debug")
```

Supports levels "debug", "info", "warning", "error", "critical". Defaults to "info".