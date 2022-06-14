import pytest
from src.app.main import main


def test_main() -> None:
    assert main() is None

#file loading tests
