import pytest
import os
import pandas as pd
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

def test_dict_can_be_loaded_to_df():
    file = file_handling()
    am = pd.DataFrame.from_dict(file.alpha_event_mappings['data'])
    assert len(am) == 372

#mapping data from def

def test_map_alpha_and_beta_events_by_canonical_ID():
    file = file_handling()
    alpha_map = pd.DataFrame.from_dict(file.alpha_event_mappings['data'])
    beta_map = pd.DataFrame.from_dict(file.beta_event_mappings['data'])
    c_map =  pd.merge(alpha_map,beta_map,how='inner',on=['canonical_event_id'])
    assert len(c_map) == 361
