"""
Unit tests for selected utilities in Zero2Neuro's plugin_base module.

These tests verify required plugin arguments and the parsing of inline
plugin arguments. The tests focus on small behaviors that can be tested
independently from the larger plugin environment.
"""

import pytest

from plugin_base import require
from plugin_base import GenericPlugin

def test_require_returns_existing_value():
    """Verify that require() returns the value of an existing argument."""
    data = {"name": "Zero2Neuro"}

    result = require(data, "name")

    assert result == "Zero2Neuro"


def test_require_raises_error_for_missing_key():
    """Verify that require() raises ValueError when an argument is missing."""
    data = {"name": "Zero2Neuro"}

    with pytest.raises(ValueError):
        require(data, "missing")

def test_parse_args_inline_key_value():
    """Verify parsing of an inline key=value plugin argument."""
    plugin = GenericPlugin()
    plugin.parser.add_argument("--method")

    plugin.parse_args_inline("method=minmax")

    assert plugin.args.method == "minmax"


def test_parse_args_inline_flag():
    """Verify parsing of an inline Boolean flag without an explicit value."""
    plugin = GenericPlugin()
    plugin.parser.add_argument("--verbose", action="store_true")

    plugin.parse_args_inline("verbose")

    assert plugin.args.verbose is True