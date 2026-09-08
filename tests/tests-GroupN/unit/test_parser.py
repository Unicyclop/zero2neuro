from parser import CommentedArgumentParser


def test_convert_arg_line_skips_blank_line():
    parser = CommentedArgumentParser()

    result = parser.convert_arg_line_to_args("   ")

    assert result == []


def test_convert_arg_line_removes_comment():
    parser = CommentedArgumentParser()

    result = parser.convert_arg_line_to_args("--epochs # training epochs")

    assert result == ["--epochs"]


def test_convert_arg_line_handles_option_equals_value():
    parser = CommentedArgumentParser()

    result = parser.convert_arg_line_to_args("--experiment_name=my experiment")

    assert result == ["--experiment_name", "my experiment"]


def test_convert_arg_line_preserves_value_whitespace():
    parser = CommentedArgumentParser()

    result = parser.convert_arg_line_to_args("my experiment name   ")

    assert result == ["my experiment name"]