import folium
from folium.plugins import HeatMap

from api.earthquake_prediction_data_cleaning import EarthquakePredictionDataCleaning


class EarthquakeAndTectonicPlatesVisualisations(EarthquakePredictionDataCleaning):

    def visualise_tectonic_plate(self):
        tectonic = folium.Map(tiles="cartodbpositron", zoom_start=5)

        plates = list(self.tectonic_plate_data_frame["plate"].unique())
        for plate in plates:
            plate_vals = self.tectonic_plate_data_frame[self.tectonic_plate_data_frame["plate"] == plate]
            latitudes = plate_vals["lat"].values
            longitudes = plate_vals["lon"].values
            points = list(zip(latitudes, longitudes))
            indexes = [None] + [i + 1 for i, x in enumerate(points) if
                                i < len(points) - 1 and abs(x[1] - points[i + 1][1]) > 300] + [None]
            for i in range(len(indexes) - 1):
                folium.vector_layers.PolyLine(points[indexes[i]:indexes[i + 1]], popup=plate, color="red",
                                              fill=False, ).add_to(tectonic)

        return tectonic

    def visualise_earthquakes_on_tectonic_plate(self):
        plot = folium.Map(tiles="cartodbpositron", zoom_start=5)
        gradient = {.33: "darkred", .66: "#ef5675", 1: "#ffa600"}
        plates = list(self.tectonic_plate_data_frame["plate"].unique())
        for plate in plates:
            plate_vals = self.tectonic_plate_data_frame[self.tectonic_plate_data_frame["plate"] == plate]
            lats = plate_vals["lat"].values
            lons = plate_vals["lon"].values
            points = list(zip(lats, lons))
            indexes = [None] + [i + 1 for i, x in enumerate(points) if i < len(points) - 1 and abs(x[1] - points[i + 1][1]) > 300] + [None]
            for i in range(len(indexes) - 1):
                folium.vector_layers.PolyLine(points[indexes[i]:indexes[i + 1]], popup=plate, fill=False, color="red").add_to(plot)
                HeatMap(data=self.earthquake_data_frame[["Latitude", "Longitude"]], hue="Magnitude", min_opacity=0.5,
                        radius=1, gradient=gradient).add_to(plot)
        return plot

    def visualise_predicted_earthquake_on_tectonic_plate(self, predicted_earthquake_data_frame):
        plot = folium.Map(tiles="cartodbpositron", zoom_start=5)
        gradient = {.33: "blue", .66: "#ef5675", 1: "#ffa600"}
        plates = list(self.tectonic_plate_data_frame["plate"].unique())
        for plate in plates:
            plate_vals = self.tectonic_plate_data_frame[self.tectonic_plate_data_frame["plate"] == plate]
            lats = plate_vals["lat"].values
            lons = plate_vals["lon"].values
            points = list(zip(lats, lons))
            indexes = [None] + [i + 1 for i, x in enumerate(points) if i < len(points) - 1 and abs(x[1] - points[i + 1][1]) > 300] + [None]
            for i in range(len(indexes) - 1):
                folium.vector_layers.PolyLine(points[indexes[i]:indexes[i + 1]], popup=plate, fill=False, color="red").add_to(plot)
                HeatMap(data=predicted_earthquake_data_frame[["lat", "lon"]], hue="Magnitude", min_opacity=0.5, radius=1, gradient=gradient).add_to(plot)
        return plot
