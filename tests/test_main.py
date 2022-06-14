import pytest
import os
from src.app.main import main
from src.app.app_functions import file_handling


def test_main() -> None:
    assert main() is None

#file loading tests


def test_if_we_can_see_local_files():
    file = 'toy_data/alpha_event_mappings.csv'
    assert file is not None


def test_if_csv_is_loaded_into_df():
    file = file_handling()
    file.open_file_to_df('toy_data/alpha_event_mappings.csv')
    assert file is not None


def test_all_csvs_can_be_loaded():
    file = file_handling()
    assert len(file.data) == 8

#mapping data from def


def test_map_alpha_event_mapping():
    file = file_handling()
    am = file.data['alpha_event_mappings']
    count = am.canonical_event_id.unique()
    assert len(count) == 372


def test_map_alpha_and_beta_events_by_canonical_ID():
    pass
