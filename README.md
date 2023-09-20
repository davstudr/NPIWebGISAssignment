# NPIWebGISAssignment

#### David Studer
#### davidstuder@gmx.ch
#### +47 927 71 252

## Objective
This README.md document explains the workflow for the Web-Gis-Assignment.
Each folder in the repository contains scripts and data necessary to complete one task. In addition to this document code is enriched with comments. The Assignment was done using MacOS. Some installation might differ on Windows or Linux.

# 1-DataProcessing
To convert the wind.csv file to a geosjon open the csvTOgeojson.py file. For running the file you need to have python installed inluding the geojson package. If you are using the Anaconda distribution you can use the following command in your terminal for installing geojson (macOS): #conda install -c conda-forge geojson#

Bonus: For guaranteeing the integrity of the processed information the csv_to_geojson funciton includes a try statement to validate 

Demonstrate which techniques could be used to guarantee the integrity of processed information. How would you ensure the processing pipeline is reproducible in case files have to be reprocessed later?

# 2-DataStorage
For storing the wind.json file in a postgresql/postGIS databse the following steps were necessary:

- Install postgresql
- Install PgAdmin4
- Setup new Server (WindServer) and database (wind_data) and add postgis extension (CREATE EXTENSION postgis) in PgAdmin4 
- Install gdal using: conda install -c conda-forge gdal or brew install gdal
- Change terminal directory to 2-DataStorage folder: cd /Users/davidstuder/Projects/3\ NPI\ Assignment/2-DataStorage/      
- Run command: ogr2ogr -f "PostgreSQL" PG:"dbname=wind_data user=davidstuder" wind.json -nln wind_table - Uploads wind.json file into wind_data databse  
- In pgAdmin4 SELECT '*' FROM wind_table to view data table

After processing the raw data it should be ingested into a database. It is your choice in which database to ingest the information.
If you choose to work with PostgreSQL/PostGIS provide a script that loads the data into DB. Assume the DB is running on a localhost. Explain how to run loading script. You can provide a docker compose file if you prefer to work with containerized instances.

Alternatively you can use sqlite, geopackage or similar. *Please explain your choice of data storage backend*. 
Pay attention to selecting right the CRS.

# 3-DataPublication

## Question: When you would publish the data as WFS and when as WMS, and when you would use both?
WMS (Web Map Service):
Is used when the goal is to display static or dynamically generated maps as rasters. It simplifies the map rendering and the visualization and therefore reduces the amount of data that has to be loaded because it is able to send pre-rendered images.

WFS (Web Feature Servie):
Is used when the goal is to display vector data where the indivicual geospatial feature has to be selected, edited or queried. 

Combining WMS and WFS:
A WMS Service can for example be used to display a basemap while the WFS Service offers access to additional data that can be queried and edited.

## Publish WMS & WFS Layer
To publish whe WMS and WDS layer the following steps were necessary:

- Install GeoServer
- More detailed see word document: READMEAPPENDIX.docx


Using the storage  generated in the previous step please publish the data as both WMS and WFS layers. 

Suggestion: You can solve this task by installing a geoserver instance on your local machine. In such case please provide screenshots and text summary explaining data publishing steps. Alternatively you can provide a docker compose file that sets a geoserver instance and a script that publishes the data using Geoservers REST API. You can also use a public service like QGIS cloud to publish WMS and WFS layers. Please provide
a summary how you have published the data including text and screenshots.


# 4-DataVisualization


- Establish WFS Connection from QGIS to GeoServer - Error, Attribute names had to be renamed so that they did not contain any spaces. That was done using pgAdmin4.
- Styling of Wind Data points.
- Add Sentinel2 Basemap using the https://tiles.maps.eox.at/wms WMS Service that provides cloudless Sentinel-2 images. 
- Add Antarctic coastline WMS Service from https://maps.bas.ac.uk/antarctic/wms
- Filter for points that are in the Dronning Maud Land region

Please create a QGIS project that uses published previously WFS layer. Use only the data points that fall into the Dronning Maud Land region. Please add a basemap, e.g. MODIS or Sentinel-2 satellite mosaic as a background, and a WFS layer containing coastline or other information that helps identifying the location. 

Generate a specific style for displaying the data. Export the project file, SLD and QLD styles and add them to the deliverable package/repository. QGIS project here is used as a replacement for a web client.



CARTO:
Using a web mapping application illustrating the layers mentiond above is a bonus. In such case provide a link to the app/fiddle, image tag if application is published as a Docker image, or add source code for the application to the project.
