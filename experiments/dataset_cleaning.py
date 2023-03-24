# Completion pending success of experiment

import pandas as pd
class DataCleaning:
    def __init__(self):
        self.earthquake_data_frame = {}
        self.tectonic_plate_data_frame = {}

    def handle(self):
        self.__loadDataSet()
        self.__remove_record_with_missing_features()
        self.__remove_record_with_wrong_dates()

    def __loadDataSet(self):
        self.earthquake_data_frame = pd.read_csv('../datasets/earth_quakes_dataset.csv')
        self.tectonic_plate_data_frame = pd.read_csv('../datasets/earth_quakes_dataset.csv')

    def __remove_record_with_missing_features(self):
        rows_with_missing_column_value = [col for col in self.earthquake_data_frame.columns if self.earthquake_data_frame[col].isnull().any()]
        self.earthquake_data_frame = self.earthquake_data_frame.drop(rows_with_missing_column_value, axis=1)

    def __remove_record_with_wrong_dates(self):
        return ""


