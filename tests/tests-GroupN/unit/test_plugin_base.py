import pytest

from plugin_base import require
from plugin_base import GenericPlugin

def test_require_returns_existing_value():
    data = {"name": "Zero2Neuro"}

    result = require(data, "name")

    assert result == "Zero2Neuro"


def test_require_raises_error_for_missing_key():
    data = {"name": "Zero2Neuro"}

    with pytest.raises(ValueError):
        require(data, "missing")

def test_parse_args_inline_key_value():
    plugin = GenericPlugin()
    plugin.parser.add_argument("--method")

    plugin.parse_args_inline("method=minmax")

    assert plugin.args.method == "minmax"


def test_parse_args_inline_flag():
    plugin = GenericPlugin()
    plugin.parser.add_argument("--verbose", action="store_true")

    plugin.parse_args_inline("verbose")

    assert plugin.args.verbose is True