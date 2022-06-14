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
    alpha_map = file.alpha_event_mappings
    assert len(alpha_map) == 372

#mapping data from def


def test_map_alpha_and_beta_events_by_canonical_ID():
    file = file_handling()
    alpha_map = file.alpha_event_mappings
    beta_map = file.beta_event_mappings
    c_map = pd.merge(alpha_map, beta_map, how='inner', on=['canonical_event_id'])
    assert len(c_map) == 361

@pytest.mark.skip(reason="still in development")
def test_create_alpha_and_beta_event_C_ID_unique_lists():
    alpha_list = []
    beta_list = []
    assert alpha_list == 358 and beta_list == 361

@pytest.mark.skip(reason="still in development")
def test_alpha_event_list_missing_c_ID():
    test = []
    assert test == 14

@pytest.mark.skip(reason="still in development")
def test_beta_event_list_missing_c_ID():
    test = []
    assert test == 33

@pytest.mark.skip(reason="still in development")
def test_alpha_and_beta_events_can_be_zipped_into_one_dict():
    assert type(test_a) is dict and type(test_b) is dict

@pytest.mark.skip(reason="still in development")
def test_map_alpha_and_beta_teams_by_canonical_ID():
    file = file_handling()
    alpha_map = file.alpha_event_mappings
    beta_map = file.beta_event_mappings
    c_map = pd.merge(alpha_map, beta_map, how='inner', on=['canonical_event_id'])
    assert len(c_map) == 23

@pytest.mark.skip(reason="still in development")
def test_alpha_team_list_missing_c_ID():
    test = []
    assert test == 34

@pytest.mark.skip(reason="still in development")
def test_beta_team_list_missing_c_ID():
    test = []
    assert test == 42

@pytest.mark.skip(reason="still in development")
def test_alpha_and_beta_teams_can_be_zipped_into_one_dict():
    assert type(test_a) is dict and type(test_b) is dict

@pytest.mark.skip(reason="still in development")
def test_mapping_alpha_totals_to_c_ID_using_alpha_dictionary():
    test = []
    assert len(test) == 322

@pytest.mark.skip(reason="still in development")
def test_mapping_alpha_reviews_to_c_ID_using_alpha_dictionary():
    test = []
    assert len(test) == 323

@pytest.mark.skip(reason="still in development")
def test_mapping_alpha_reviews_teams_to_c_ID_using_alpha_team_dictionary():
    test = []
    assert len(test) == 323

@pytest.mark.skip(reason="still in development")
def test_mapping_beta_fixtures_to_c_ID_using_beta_event_dictionary():
    test = []
    assert len(test) == 325

@pytest.mark.skip(reason="still in development")
def test_mapping_beta_teams_fixtures_to_c_ID_using_beta_team_dictionary():
    test = []
    assert len(test) == 325

@pytest.mark.skip(reason="still in development")
def test_mapping_beta_market_to_c_ID_using_beta_event_dictionary():
    test = []
    assert len(test) == 324

@pytest.mark.skip(reason="still in development - Check one")
def test_check_for_goal_outliers():
    test = []
    assert len(test) == 2

@pytest.mark.skip(reason="still in development - Check one")
def test_check_for_goal_outliers():
    test = []
    assert len(test) == 2

@pytest.mark.skip(reason="still in development - Check two")
def test_check_for_kickoff_time_outliers():
    test = []
    assert len(test) == 0

@pytest.mark.skip(reason="still in development - Check three")
def test_check_for_jackpot_potential():
    test = []
    assert len(test) == 2
#
