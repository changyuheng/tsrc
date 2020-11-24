from cli_ui.tests import MessageRecorder

from tsrc.test.helpers.cli import CLI


def test_version(tsrc_cli: CLI, message_recorder: MessageRecorder) -> None:
    tsrc_cli.run("version")
    assert message_recorder.find("version")
