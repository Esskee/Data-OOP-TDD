import pandas as pd


class file_handling():

    def __init__(self):
        self.data = self.save_csvs_to_dict()

        self.alpha_event_mappings = self.open_file_to_df('toy_data/alpha_event_mappings.csv')
        self.beta_event_mappings = self.open_file_to_df('toy_data/beta_event_mappings.csv')
        self.alpha_reviews = self.open_file_to_df('toy_data/alpha_reviews.csv')
        self.alpha_team_mappings = self.open_file_to_df('toy_data/alpha_team_mappings.csv')
        self.beta_team_mappings = self.open_file_to_df('toy_data/beta_team_mappings.csv')
        self.alpha_totals = self.open_file_to_df('toy_data/alpha_totals.csv')
        self.beta_fixtures = self.open_file_to_df('toy_data/beta_fixtures.csv')
        self.beta_market = self.open_file_to_df('toy_data/beta_market.csv')

    #importing local csv files into memory
    def open_file_to_df(self, file_name):
        file = pd.read_csv(file_name, low_memory=False)
        return file

    def save_csvs_to_dict(self):
        files = {'alpha_event_mappings': 'toy_data/alpha_event_mappings.csv', 'beta_event_mappings': 'toy_data/beta_event_mappings.csv', 'alpha_review': 'toy_data/alpha_reviews.csv', 'alpha_team_mappings': 'toy_data/alpha_team_mappings.csv',
                 'alpha_totals': 'toy_data/alpha_totals.csv', 'beta_fixtures': 'toy_data/beta_fixtures.csv', 'beta_market': 'toy_data/beta_market.csv', 'beta_team_mappings': 'toy_data/beta_team_mappings.csv'}
        dfs = []
        for k, v in files.items():
            df = self.open_file_to_df(v)
            dfs.append({'name': k, 'data': df})
        return dfs

    def create_canonical_ID_map(self, map_type):
        map = []
        if map_type == 'event':
            map = pd.merge(self.alpha_event_mappings, self.beta_event_mappings, how='inner', on=['canonical_event_id'])
        elif map_type == 'team':
            map = pd.merge(self.alpha_team_mappings, self.beta_team_mappings, how='inner', on=['canonical_team_id'])
        else:
            raise ValueError(f'{map_type} is not a valid type')
        return map

    def create_canonical_ID_list(self, map):
        sample = map.canonical_event_id.unique()
        return sample
