import pandas as pd


class file_handling():

    def __init__(self):
        self.data = self.save_csvs_to_dict()

    #importing local csv files into memory
    def open_file_to_df(self, file_name):
        file = pd.read_csv(file_name, low_memory=False)
        return file

    def save_csvs_to_dict(self):
        files = {'alpha_event_mappings': 'toy_data/alpha_event_mappings.csv', 'beta_event_mappings': 'toy_data/beta_event_mappings.csv', 'alpha_review': 'toy_data/alpha_reviews.csv', 'alpha_team_mappings': 'toy_data/alpha_team_mappings.csv',
                 'alpha_totals': 'toy_data/alpha_totals.csv', 'beta_fixtures': 'toy_data/beta_fixtures.csv', 'beta_market': 'toy_data/beta_market.csv', 'beta_team_mappings': 'toy_data/beta_team_mappings.csv'}
        data_frames = []
        for k, v in files.items():
            df = self.open_file_to_df(v)
            data_frames.append({k: df})
        return data_frames
