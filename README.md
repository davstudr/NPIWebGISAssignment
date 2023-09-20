# NPI Web GIS Assignment

#### David Studer
#### Email: davidstuder@gmx.ch
#### Tlf: +47 927 71 252

## Objective
This README.md document explains the workflow for the Web-Gis-Assignment.
Each folder in the repository contains scripts and data necessary to complete one task. In addition to this document code is enriched with comments. The Assignment was done using MacOS. Some installations might differ on Windows or Linux.

# 1-DataProcessing
To convert the wind.csv file to a geosjon open the csvTOgeojson.py file. For running the file, you need to have python installed including the geojson package. If you are using the Anaconda distribution, you can use the following command in your terminal for installing geojson (macOS): ```conda install -c conda-forge geojson```

Bonus: For guaranteeing the integrity of the processed information the csv_to_geojson function includes a try statement to validate each data entry. Several data entries were excluded due to wrong data formats.

# 2-DataStorage
For storing the wind.json file in a postgresql/postGIS database the following steps were necessary:
- Install postgresql
- Install PgAdmin4
- Setup new Server (WindServer) and database (wind_data) and add postgis extension ```CREATE EXTENSION postgis``` in PgAdmin4
- Install gdal using: ```conda install -c conda-forge gdal``` or ```brew install gdal```
- To upload geojson to postgresql/postgis, change terminal directory to 2-DataStorage folder: ```cd /Users/davidstuder/Projects/3\ NPI\ Assignment/2-DataStorage/```    
- Run command: ```ogr2ogr -f "PostgreSQL" PG:"dbname=wind_data user=davidstuder" wind.json -nln wind_table``` - Uploads wind.json file into wind_data database
- In pgAdmin4 ```SELECT * FROM wind_table``` to view data table
- <img width="1507" alt="Screenshot 2023-09-19 at 18 44 44" src="https://github.com/davstudr/NPIWebGISAssignment/assets/145550823/86a6422e-d2cd-40bf-82bd-43a865c7e0ad">


# 3-DataPublication

## Question: When would you publish the data as WFS and when as WMS, and when would you use both?
WMS (Web Map Service):
Is used when the goal is to display static or dynamically generated maps as rasters. It simplifies the map rendering and the visualization and therefore reduces the amount of data that must be loaded because it is able to send pre-rendered images.

WFS (Web Feature Servie):
Is used when the goal is to display vector data where the individual geospatial feature must be selected, edited or queried. 

Combining WMS and WFS:
A WMS Service can for example be used to display a basemap while the WFS Service offers access to additional data that can be queried and edited.

## Publish WMS & WFS Layer
To publish the WMS and WFS layer the following steps were necessary:
- Install GeoServer
- Create a new Workspace (enable WMS & WFS) and a new store in GeoServer and connect to Postgresql wind_data database.
- <img width="755" alt="Screenshot 2023-09-19 at 19 17 29" src="https://github.com/davstudr/NPIWebGISAssignment/assets/145550823/c7819bf0-04aa-4755-b62f-69a695eae598">
- Create new Layer and Publish Layer.
- <img width="1263" alt="Screenshot 2023-09-19 at 19 21 07" src="https://github.com/davstudr/NPIWebGISAssignment/assets/145550823/4031ccf4-0039-4175-8bb8-9d3382a84778">

# 4-DataVisualization
- Establish WFS Connection from QGIS to GeoServer (using Localhost: ```http://localhost:8080/geoserver/ows?acceptversions=2.0.0```) - an Error occurred, Attribute names had to be renamed so that they did not contain any spaces. That was done in postgresql using pgAdmin4.
- Styling of Wind Data points including export of sld style file.
- Add Sentinel 2 Basemap using the https://tiles.maps.eox.at/wms WMS Service that provides cloudless Sentinel-2 images. 
- Add Antarctic coastline WMS Service from https://maps.bas.ac.uk/antarctic/wms
- Filter for points that are in the Dronning Maud Land region - Unfortunately no WFS Service or Geojson file of Dronning Maud Land could be found, therefore I skipped this step. If a file could have been found a simple Clip function in QGIS could have been used to exclude all points outside of Dronning Maud Land.
- <img width="1504" alt="image" src="https://github.com/davstudr/NPIWebGISAssignment/assets/145550823/9a92cb4c-5dac-464f-8b00-cb2590e86d1b">

Bonus:
Using CARTO to visualize the wind speed in Antarctica:
- ```"https://pinea.app.carto.com/map/ef58381d-996d-4427-8fed-fcaa0d4d0dd4"```
