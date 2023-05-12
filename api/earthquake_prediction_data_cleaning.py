import pandas as pd
from scipy.spatial import KDTree
from flask import Flask, jsonify


class EarthquakePredictionDataCleaning:

    def __init__(self):
        self.__load_dataset__()
        self.__clean_dataset__()
        self.__get_only_earthquakes__()
        self.__remove_bad_date_and_time__()
        self.__combine_data_sets__()
        self.__prepare_json_response__()

    def __load_dataset__(self):
        self.earthquake_data_frame = pd.read_csv('datasets/earth_quakes_dataset.csv')
        self.tectonic_plate_data_frame = pd.read_csv('datasets/tectonic_plates_dataset.csv')

    def __clean_dataset__(self):
        not_needed_columns_to_drop = ['Depth Error', 'Depth Seismic Stations', 'Magnitude Type', 'Magnitude Error',
                                      'Magnitude Seismic Stations', 'Azimuthal Gap', 'Horizontal Distance',
                                      'Horizontal Error', 'Root Mean Square', 'Source', 'Magnitude Source', 'Status',
                                      'ID']
        self.earthquake_data_frame.drop(not_needed_columns_to_drop, axis=1, inplace=True)

    def __get_only_earthquakes__(self):
        self.earthquake_data_frame = self.earthquake_data_frame[self.earthquake_data_frame['Type'] == "Earthquake"].reset_index(drop=True)

    def __remove_bad_date_and_time__(self):
        self.earthquake_data_frame.loc[3359, "Date"] = "02/23/1975"
        self.earthquake_data_frame.loc[7384, "Date"] = "04/28/1985"
        self.earthquake_data_frame.loc[20470, "Date"] = "03/13/2011"
        self.earthquake_data_frame.loc[3359, "Time"] = "02:58:41"
        self.earthquake_data_frame.loc[7384, "Time"] = "02:53:41"
        self.earthquake_data_frame.loc[20470, "Time"] = "02:23:34"
        self.earthquake_data_frame['Time'] = pd.to_timedelta(self.earthquake_data_frame['Time'])
        self.earthquake_data_frame['Date'] = pd.to_datetime(self.earthquake_data_frame["Date"])

    def __combine_data_sets__(self):
        tree = KDTree(self.tectonic_plate_data_frame[['lat', 'lon']])
        distances, indices = tree.query(self.earthquake_data_frame[['Latitude', 'Longitude']], k=1)
        self.combined_data = pd.concat([self.earthquake_data_frame.reset_index(drop=True),
                                        self.tectonic_plate_data_frame.loc[indices].reset_index(drop=True)], axis=1)

    def __prepare_json_response__(self):
        self.json_earthquake_data_frame = self.earthquake_data_frame.to_json(orient='records')
        self.json_tectonic_plate_data_frame = self.tectonic_plate_data_frame.to_json(orient='records')
        self.json_combined_data = self.combined_data.to_json(orient='records')

    def get_combined_data(self):
        return jsonify(self.json_combined_data), 200

    def get_cleaned_earthquake_data(self):
        return jsonify(self.json_earthquake_data_frame), 200

    def get_cleaned_tectonic_plate_data(self):
        return jsonify(self.json_tectonic_plate_data_frame), 200
