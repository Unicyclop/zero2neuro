"""
Unit tests for selected behavior in Zero2Neuro's plugin_manager module.

These tests verify plugin-file lookup and plugin application behavior.
Small fake plugin objects are used where necessary to test PluginManager
independently from real plugin implementations.
"""

import os
import pytest

from plugin_manager import PluginManager


def test_find_plugin_file_with_existing_path(tmp_path):
    """Verify that an existing plugin path resolves to its absolute path."""
    plugin_file = tmp_path / "sample_plugin.py"
    plugin_file.write_text("# test plugin")

    manager = PluginManager([])

    result = manager._find_plugin_file(str(plugin_file))

    assert result == os.path.abspath(str(plugin_file))


def test_find_plugin_file_missing_path():
    """Verify that a missing plugin file raises FileNotFoundError."""
    manager = PluginManager([])

    with pytest.raises(FileNotFoundError):
        manager._find_plugin_file("does_not_exist.py")

def test_apply_plugins_only_runs_matching_role():
    """Verify that only plugins matching the requested role are executed."""
    class FakePlugin:
        """Minimal plugin substitute used to track whether call() is executed."""
        def __init__(self, role, result):
            self.role = role
            self.result = result
            self.called = False

        def call(self, **kwargs):
            self.called = True
            return self.result

    matching_plugin = FakePlugin(
        role="preprocess",
        result={"value": 10}
    )

    other_plugin = FakePlugin(
        role="report",
        result={"value": 20}
    )

    manager = PluginManager([])
    manager.plugins = [matching_plugin, other_plugin]

    result = manager.apply_plugins(
        "preprocess",
        value=1
    )

    assert matching_plugin.called is True
    assert other_plugin.called is False
    assert result["value"] == 10

def test_apply_plugins_handles_none_result():
    """Verify that existing values remain when a plugin returns None."""
    class FakePlugin:
        """Minimal plugin substitute that returns no replacement result."""
        def __init__(self):
            self.role = "preprocess"

        def call(self, **kwargs):
            return None

    manager = PluginManager([])
    manager.plugins = [FakePlugin()]

    result = manager.apply_plugins(
        "preprocess",
        value=5
    )

    assert result["value"] == 5