from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from api.earthquake_prediction_data_cleaning import EarthquakePredictionDataCleaning
from flask import jsonify
import pandas as pd


class PredictLocationWithLSTM(EarthquakePredictionDataCleaning):

    def __init__(self, date):
        super().__init__()
        self.date = date
        formatted_date = pd.to_datetime(date)
        self.day_of_week = formatted_date.day
        self.month = formatted_date.month
        self.year = formatted_date.year
        self.__prepare_for_prediction__()
        self.__breakdown_date_for_depth_magnitude_prediction__()
        self.__train_test_split_for_depth_magnitude_prediction__()
        self.__get_prediction_for_depth_and_magnitude__()
        self.__build_predicted__()

    def handle(self):
        return self.__response__()

    def __prepare_for_prediction__(self):
        self.predicted_locations_df = pd.read_csv('datasets/predicted_locations.csv')
        self.predicted_locations_df.columns = ['Date', 'lat', 'lon']
        predicted_date_location = [[
            self.predicted_locations_df.loc[self.predicted_locations_df['Date'] == self.date, 'lat'].values[0],
            self.predicted_locations_df.loc[self.predicted_locations_df['Date'] == self.date, 'lon'].values[0],
            self.day_of_week, self.month, self.year
        ]]
        self.x_2_pred = pd.DataFrame(predicted_date_location)
        self.x_2_pred = self.x_2_pred.set_axis(['lat', 'lon', 'DayOfWeek', 'Month', 'Year'], axis=1)

    def __breakdown_date_for_depth_magnitude_prediction__(self):
        self.combined_data = self.combined_data.drop(['Location Source', 'Type', 'Time', 'plate', 'Longitude', 'Latitude'], axis=1)
        self.combined_data['DayOfWeek'] = self.combined_data['Date'].dt.day
        self.combined_data['Month'] = self.combined_data['Date'].dt.month
        self.combined_data['Year'] = self.combined_data['Date'].dt.year
        self.combined_data = self.combined_data.drop(['Date'], axis=1)

    def __train_test_split_for_depth_magnitude_prediction__(self):
        x2 = self.combined_data.drop(['Magnitude', 'Depth'], axis=1)
        y2 = self.combined_data[['Magnitude', 'Depth']]
        self.x_2_train, self.x_2_test, self.y_2_train, self.y_2_test = train_test_split(x2, y2, test_size=0.3, random_state=42)

    def __get_prediction_for_depth_and_magnitude__(self):
        self.model2 = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, max_depth=10, min_samples_split=2, min_samples_leaf=1,max_features='sqrt', bootstrap=True, random_state=42))
        self.model2.fit(self.x_2_train, self.y_2_train)
        self.y_2_pred = self.model2.predict(self.x_2_pred)
        self.model2_depth_magnitude_pred_df = pd.DataFrame(self.y_2_pred)
        self.model2_depth_magnitude_pred_df.columns = ['Magnitude', 'Depth']

    def __build_predicted__(self):
        predicted = [[
            self.model2_depth_magnitude_pred_df.loc[0, 'Magnitude'],
            self.model2_depth_magnitude_pred_df.loc[0, 'Depth'],
            self.predicted_locations_df.loc[self.predicted_locations_df['Date'] == self.date, 'lat'].values[0],
            self.predicted_locations_df.loc[self.predicted_locations_df['Date'] == self.date, 'lon'].values[0],
            self.day_of_week, self.month, self.year
        ]]
        predicted = pd.DataFrame(predicted)
        self.predicted = predicted.set_axis(['Magnitude', 'Depth', 'lat', 'lon', 'DayOfWeek', 'Month', 'Year'], axis=1)

    def __response__(self):
        self.predicted = self.predicted.to_json(orient='records')
        return jsonify(self.predicted), 200
