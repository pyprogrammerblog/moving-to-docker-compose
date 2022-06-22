from source import __version__
from source.main import main


def test_version():
    assert __version__ == "0.1.0"


def test_main():
    """Test main returns a double quoted string"""
    assert "Hello World" == main()
