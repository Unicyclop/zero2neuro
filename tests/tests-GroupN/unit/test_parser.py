"""
Unit tests for selected command-line parsing behavior in Zero2Neuro.

These tests exercise CommentedArgumentParser.convert_arg_line_to_args()
with blank lines, comments, option/value pairs, and values containing
whitespace.
"""

from parser import CommentedArgumentParser


def test_convert_arg_line_skips_blank_line():
    """Verify that a blank argument line produces no arguments."""
    parser = CommentedArgumentParser()

    result = parser.convert_arg_line_to_args("   ")

    assert result == []


def test_convert_arg_line_removes_comment():
    """Verify that text following a comment marker is excluded."""
    parser = CommentedArgumentParser()

    result = parser.convert_arg_line_to_args("--epochs # training epochs")

    assert result == ["--epochs"]


def test_convert_arg_line_handles_option_equals_value():
    """Verify that --option=value input is separated into option and value."""
    parser = CommentedArgumentParser()

    result = parser.convert_arg_line_to_args("--experiment_name=my experiment")

    assert result == ["--experiment_name", "my experiment"]


def test_convert_arg_line_preserves_value_whitespace():
    """Verify that internal whitespace in an argument value is preserved."""
    parser = CommentedArgumentParser()

    result = parser.convert_arg_line_to_args("my experiment name   ")

    assert result == ["my experiment name"]