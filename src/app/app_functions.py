import pandas as pd


class file_handling():

    #importing local csv files into memory
    def open_file_to_df(file_name):
        file = pd.read_csv(file_name, low_memory=False)
        return file
