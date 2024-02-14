from pytodo.cli import get_version

def test_get_version():
    args = True
    assert get_version(args) == "0.0.1"
