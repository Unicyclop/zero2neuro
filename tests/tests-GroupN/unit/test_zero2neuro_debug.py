"""
Unit tests for Zero2Neuro's debugging and error-handling utilities.

These tests verify output behavior at different debug thresholds and
confirm that handle_error() terminates execution with SystemExit.
"""

import pytest

from zero2neuro_debug import print_debug, handle_error


def test_print_debug_prints_when_level_meets_threshold(capsys):
    """Verify that a debug message is printed when the threshold is met."""
    print_debug(
        "test message",
        debug_level=2,
        threshold=1
    )

    captured = capsys.readouterr()

    assert "test message" in captured.out


def test_print_debug_does_not_print_below_threshold(capsys):
    """Verify that a debug message is suppressed below the threshold."""
    print_debug(
        "hidden message",
        debug_level=0,
        threshold=1
    )

    captured = capsys.readouterr()

    assert "hidden message" not in captured.out


def test_handle_error_exits_program():
    """Verify that handle_error() terminates execution with SystemExit."""
    with pytest.raises(SystemExit):
        handle_error("test error", verbosity=0)