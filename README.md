# GlobalHappinessScore
Data pipeline for world happiness data
# Installation needed and libraries used
 Python3  
 Jupyter Lab  
 sqlite3  
 sqlalchemy  
 numpy  
 pandas  
 geopandas  
 # Files and Folders
 dataFiles folder contains the original raw data in csv and json format  
 tranform.ipynb in package transform contains all functions used for data cleaning  
 A transform.py is created from tranform.ipynb so that it can be imported in other modules  
 extract_files.ipynb:  
      - Loads the csv files and json file  
      - Clean the data  
      - Output the cleaned data in csv format in files happiness.csv and country.csv     
  create_database.ipynb create the database GlobalHappiness using happiness.csv and country.csv  
  filter.ipynb produced report_one in csv and parquet formats  
  json_output.ipynb produces report_BCM.json      
  evolution_viz.ipynb maps the yearly happiness score data in a world map
  
