import pytest
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

@pytest.fixture()
def data_init():
    file = file_handling()
    return file

@pytest.mark.usefixtures("data_init")
def test_map_alpha_and_beta_events_by_canonical_ID(data_init):
    c_map = data_init.create_canonical_ID_map('event')
    assert len(c_map) == 361

@pytest.mark.usefixtures("data_init")
def test_create_alpha_and_beta_event_C_ID_unique_lists(data_init):
    c_map = data_init.create_canonical_ID_map('event')
    alpha_list = c_map.alpha_event_id.unique()
    beta_list = c_map.beta_event_id.unique()
    assert len(alpha_list) == 358 and len(beta_list) == 361

@pytest.mark.usefixtures("data_init")
def test_alpha_event_list_missing_c_ID(data_init):
    c_map = data_init.create_canonical_ID_map('event')
    test_sample = data_init.create_canonical_ID_list(c_map, 'event')
    test = data_init.alpha_event_mappings[~data_init.alpha_event_mappings.canonical_event_id.isin(test_sample)]
    assert len(test) == 14

@pytest.mark.usefixtures("data_init")
def test_beta_event_list_missing_c_ID(data_init):
    c_map = data_init.create_canonical_ID_map('event')
    test_sample = data_init.create_canonical_ID_list(c_map, 'event')
    test = data_init.beta_event_mappings[~data_init.beta_event_mappings.canonical_event_id.isin(test_sample)]
    assert len(test) == 33

@pytest.mark.usefixtures("data_init")
def test_alpha_and_beta_events_can_be_zipped_into_one_dict(data_init):
    test_a, test_b = data_init.create_canonical_dictionaries('event')
    assert type(test_a) is dict and type(test_b) is dict

@pytest.mark.usefixtures("data_init")
def test_map_alpha_and_beta_teams_by_canonical_ID(data_init):
    t_map = data_init.create_canonical_ID_map('team')
    assert len(t_map) == 23

@pytest.mark.usefixtures("data_init")
def test_alpha_team_list_missing_c_ID(data_init):
    t_map = data_init.create_canonical_ID_map('team')
    test_sample = data_init.create_canonical_ID_list(t_map, 'team')
    test = data_init.alpha_team_mappings[~data_init.alpha_team_mappings.canonical_team_id.isin(test_sample)]
    assert len(test) == 34

@pytest.mark.usefixtures("data_init")
def test_beta_team_list_missing_c_ID(data_init):
    t_map = data_init.create_canonical_ID_map('team')
    test_sample = data_init.create_canonical_ID_list(t_map, 'team')
    test = data_init.beta_team_mappings[~data_init.beta_team_mappings.canonical_team_id.isin(test_sample)]
    assert len(test) == 42

@pytest.mark.usefixtures("data_init")
def test_alpha_and_beta_teams_can_be_zipped_into_one_dict(data_init):
    test_a, test_b = data_init.create_canonical_dictionaries('team')
    assert type(test_a) is dict and type(test_b) is dict

@pytest.mark.usefixtures("data_init")
def test_mapping_alpha_totals_to_c_ID_using_alpha_dictionary(data_init):
    c_map = data_init.create_canonical_ID_map('event')
    alpha_list = c_map.alpha_event_id.unique()
    alpha_totals = data_init.alpha_totals[data_init.alpha_totals['alpha_event_id'].isin(alpha_list)]
    alpha_totals['canonical_event_id'] = alpha_totals['alpha_event_id'].apply(lambda x: data_init.alpha_event_dictonary[x])
    assert len(alpha_totals) == 322

@pytest.mark.usefixtures("data_init")
def test_mapping_alpha_reviews_to_c_ID_using_alpha_dictionary(data_init):
    c_map = data_init.create_canonical_ID_map('event')
    alpha_list = c_map.alpha_event_id.unique()
    alpha_reviews = data_init.alpha_reviews[data_init.alpha_reviews['alpha_event_id'].isin(alpha_list)]
    alpha_reviews['canonical_event_id'] = alpha_reviews['alpha_event_id'].apply(lambda x: data_init.alpha_event_dictonary[x])
    assert len(alpha_reviews) == 323

@pytest.mark.usefixtures("data_init")
def test_mapping_alpha_reviews_teams_to_c_ID_using_alpha_team_dictionary(data_init):
    c_map = data_init.create_canonical_ID_map('event')
    alpha_list = c_map.alpha_event_id.unique()
    alpha_reviews = data_init.alpha_reviews[data_init.alpha_reviews['alpha_event_id'].isin(alpha_list)]
    alpha_reviews['canonical_event_id'] = alpha_reviews['alpha_event_id'].apply(lambda x: data_init.alpha_event_dictonary[x])
    alpha_reviews['canonical_team1_id'] = alpha_reviews['team1_id'].apply(lambda x: data_init.alpha_team_dictonary[x])
    alpha_reviews['canonical_team2_id'] = alpha_reviews['team2_id'].apply(lambda x: data_init.alpha_team_dictonary[x])
    assert len(alpha_reviews) == 323

@pytest.mark.usefixtures("data_init")
def test_mapping_beta_fixtures_to_c_ID_using_beta_event_dictionary(data_init):
    c_map = data_init.create_canonical_ID_map('event')
    beta_list = c_map.beta_event_id.unique()
    beta_fixtures = data_init.beta_fixtures[data_init.beta_fixtures['beta_event_id'].isin(beta_list)]
    beta_fixtures['canonical_event_id'] = beta_fixtures['beta_event_id'].apply(lambda x: data_init.beta_event_dictonary[x])
    assert len(beta_fixtures) == 325

@pytest.mark.usefixtures("data_init")
def test_mapping_beta_teams_fixtures_to_c_ID_using_beta_team_dictionary(data_init):
    c_map = data_init.create_canonical_ID_map('event')
    beta_list = c_map.beta_event_id.unique()
    beta_fixtures = data_init.beta_fixtures[data_init.beta_fixtures['beta_event_id'].isin(beta_list)]
    beta_fixtures['canonical_event_id'] = beta_fixtures['beta_event_id'].apply(lambda x: data_init.beta_event_dictonary[x])
    beta_fixtures['canonical_team1_id'] = data_init.beta_fixtures['team1_id'].apply(lambda x: data_init.beta_team_dictonary[x])
    beta_fixtures['canonical_team2_id'] = data_init.beta_fixtures['team2_id'].apply(lambda x: data_init.beta_team_dictonary[x])
    assert len(beta_fixtures) == 325

@pytest.mark.usefixtures("data_init")
def test_mapping_beta_market_to_c_ID_using_beta_event_dictionary(data_init):
    c_map = data_init.create_canonical_ID_map('event')
    beta_list = c_map.beta_event_id.unique()
    beta_market = data_init.beta_market[data_init.beta_market['beta_event_id'].isin(beta_list)]
    beta_market['canonical_event_id'] = beta_market['beta_event_id'].apply(lambda x: data_init.beta_event_dictonary[x])
    assert len(beta_market) == 324

@pytest.mark.usefixtures("data_init")
def test_check_for_goal_outliers(data_init):
    c_map = data_init.create_canonical_ID_map('event')
    alpha_list = c_map.alpha_event_id.unique()
    alpha_totals = data_init.alpha_totals[data_init.alpha_totals['alpha_event_id'].isin(alpha_list)]
    alpha_totals['canonical_event_id'] = alpha_totals['alpha_event_id'].apply(lambda x: data_init.alpha_event_dictonary[x])

    alpha_totals.isna().sum()
    missing_goals = alpha_totals.dropna(subset=['team1_goals','team2_goals'])
    missing_goals = missing_goals.canonical_event_id.unique()
    missing_goals = alpha_totals[~alpha_totals['canonical_event_id'].isin(missing_goals)]
    assert len(missing_goals) == 2

@pytest.mark.skip(reason="still in development - Check two")
def test_check_for_kickoff_time_outliers():
    test = []
    assert len(test) == 0

@pytest.mark.skip(reason="still in development - Check three")
def test_check_for_jackpot_potential():
    test = []
    assert len(test) == 2
#
