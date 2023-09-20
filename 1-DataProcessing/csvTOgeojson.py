# Import packages
import csv
# For installing geojson using Anaconda distribution use: conda install -c conda-forge geojson
import geojson

# Define csv_to_geojson function
def csv_to_geojson(input_csv_file, output_geojson_file):
    features = []
    with open(input_csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
           # CSV Error handling - skip row if data format is invalid
           try:
               timestamp = row['Timestamp']
               wind_speed = float(row['Wind Speed (m/s)'])
               u_component = float(row['U Component (m/s)'])
               v_component = float(row['V Component (m/s)'])
               latitude = float(row['Latitude (degrees)'])
               longitude = float(row['Longitude (degrees)'])

               # Create a GeoJSON feature with properties
               feature = geojson.Feature(
                   geometry=geojson.Point((longitude, latitude)),
                   properties={
                       'Timestamp': timestamp,
                       'Wind Speed (m/s)': wind_speed,
                       'U Component (m/s)': u_component,
                       'V Component (m/s)': v_component,
                   }
               )
               features.append(feature)
           except ValueError:
               print(f"Skipping row with invalid data: {row}")
            
    feature_collection = geojson.FeatureCollection(features)
    
    with open("wind.json", 'w') as geojson_file:
        geojson_file.write('%s' % feature_collection)

if __name__ == "__main__":
    input_csv_file = 'wind.csv'  # Replace with your CSV file name, CSV file has to be stored in the script folder
    output_geojson_file = 'wind.geojson'  # Replace with the desired output GeoJSON file name
    csv_to_geojson(input_csv_file, output_geojson_file)