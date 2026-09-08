import os
import pytest

from plugin_manager import PluginManager


def test_find_plugin_file_with_existing_path(tmp_path):
    plugin_file = tmp_path / "sample_plugin.py"
    plugin_file.write_text("# test plugin")

    manager = PluginManager([])

    result = manager._find_plugin_file(str(plugin_file))

    assert result == os.path.abspath(str(plugin_file))


def test_find_plugin_file_missing_path():
    manager = PluginManager([])

    with pytest.raises(FileNotFoundError):
        manager._find_plugin_file("does_not_exist.py")

def test_apply_plugins_only_runs_matching_role():
    class FakePlugin:
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
    class FakePlugin:
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