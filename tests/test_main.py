import pytest
import pandas as pd
from src.app.main import main


def test_main() -> None:
    assert main() is None
