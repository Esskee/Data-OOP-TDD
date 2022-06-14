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


def test_if_all_csvs_can_be_loaded():
    files = ['toy_data/alpha_event_mappings.csv', 'toy_data/beta_event_mappings.csv', 'toy_data/alpha_reviews.csv', 'toy_data/alpha_team_mappings.csv',
             'toy_data/alpha_totals.csv', 'toy_data/beta_fixtures.csv', 'toy_data/beta_market.csv', 'toy_data/beta_team_mappings.csv']
    file = file_handling()
    for i in files:
        file.open_file_to_df(i)
    assert len(files) == 8
