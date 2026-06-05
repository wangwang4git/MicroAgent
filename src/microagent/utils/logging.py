"""Logging setup for the MicroAgent framework."""

from __future__ import annotations

import logging


def setup_logging(level: str = "INFO", log_file: str | None = None) -> None:
    """Configure the root logger for the framework.

    Parameters:
        level: Log level (DEBUG, INFO, WARNING, ERROR).
        log_file: Optional path to a log file.
    """
    ...


def get_logger(name: str) -> logging.Logger:
    """Get a logger for a specific module."""
    ...
