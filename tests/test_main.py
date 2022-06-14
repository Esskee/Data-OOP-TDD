import pytest
import os
from src.app.main import main
from src.app.app_functions import file_handling


def test_main() -> None:
    assert main() is None

#file loading tests


def test_if_csv_is_loaded_into_df():
    file = file_handling()
    file.open_file_to_df('toy_data/alpha_event_mappings.csv')
    assert file is not None
