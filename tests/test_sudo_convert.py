from src.utils import sudo_convert


def test_command_with_sudo():
    expected = "echo password1 | sudo -S ls"
    assert sudo_convert("sudo ls", "password1") == expected


def test_command_without_sudo():
    assert sudo_convert("ls -l", "password1") == "ls -l"
