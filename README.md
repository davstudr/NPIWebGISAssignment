# NPI Web GIS Assignment

#### David Studer

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
<img width="1507" alt="ScreenshotDataStorage" src="https://github.com/davstudr/NPIWebGISAssignment/assets/145550823/c07d4bbe-2b10-4cc5-9781-8e4a5de3d491">

 ## CRS System:
 No adjustment was done to the CRS System. All processing steps were done using WGS 84 (EPSG:4326). For clipping and visualisation purposes another coordinate system more suited for the Antarctic such as the WGS84 / Antarctic Polar Stereographic (EPSG:3031) could have been the better choice.


# 3-DataPublication

## Question: When would you publish the data as WFS and when as WMS, and when would you use both?
WMS (Web Map Service):
Is used when the goal is to display static or dynamically generated maps as rasters. It simplifies the map rendering and the visualization and therefore reduces the amount of data that must be loaded because it is able to send pre-rendered images.

WFS (Web Feature Servie):
Is used when the goal is to display vector data where the individual geospatial feature must be selected, edited or queried. This is can be a heavy data loading task and reduce the performance of your application.

Combining WMS and WFS:
A WMS Service can for example be used to display a basemap while the WFS Service offers access to additional data that can be queried and edited.

## Publish WMS & WFS Layer
To publish the WMS and WFS layer the following steps were necessary:
- Install GeoServer
- Create a new Workspace (enable WMS & WFS) and a new store in GeoServer and connect to Postgresql wind_data database.
<img width="755" alt="ScreenshotDataPublication1" src="https://github.com/davstudr/NPIWebGISAssignment/assets/145550823/59ccf984-2f0d-4a91-8735-f95e257f86ec">

- Create new Layer and Publish Layer.
<img width="1263" alt="ScreenshotDataPublication2" src="https://github.com/davstudr/NPIWebGISAssignment/assets/145550823/5d33015c-70a6-4d82-b92d-8eb1508ea4f0">


# 4-DataVisualization
- Establish WFS Connection from QGIS to GeoServer (using Localhost: ```http://localhost:8080/geoserver/ows?acceptversions=2.0.0```) - an Error occurred, Attribute names had to be renamed so that they did not contain any spaces. That was done in postgresql using pgAdmin4.
- Styling of Wind Data points including export of sld style file.
- Add Sentinel 2 Basemap using the https://tiles.maps.eox.at/wms WMS Service that provides cloudless Sentinel-2 images. 
- Add Antarctic coastline WMS Service from https://maps.bas.ac.uk/antarctic/wms
- Filter for points that are in the Dronning Maud Land region - Unfortunately no WFS Service or Geojson file of Dronning Maud Land could be found, therefore I skipped this step. If a file could have been found a simple Clip function in QGIS could have been used to exclude all points outside of Dronning Maud Land.
<img width="1504" alt="Screenshot 2023-09-20 at 11 19 20" src="https://github.com/davstudr/NPIWebGISAssignment/assets/145550823/59e63147-c359-4e90-a602-5dbbc612bec2">


Bonus:
Using CARTO to visualize the wind speed in Antarctica:
- https://pinea.app.carto.com/map/ef58381d-996d-4427-8fed-fcaa0d4d0dd4
