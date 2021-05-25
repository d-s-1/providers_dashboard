# Providers Dashboard

## About
Dashboard based on 2017 Medicare provider data and built with Python's Dash library.  This app uses a SQLite backend (a table of 9M+ records) and runs on AWS using Docker & Gunicorn (4 workers).

## Feature Notes
* caching of results
* customized Excel export (user selections, raw data, charts, footnotes)
* disabling or hiding GUI components from user when not applicable
* default selection values populated when app initializes
* dropdown options filtered or cleared based on upstream selections
* help info (HCPCS descriptions) shown to user if desired
* user error messages

## Data
* Based on 2017 Medicare Provider Utilization and Payment Data accessed December 18, 2019 from data.cms.gov:  https://data.cms.gov/Medicare-Physician-Supplier/Medicare-Provider-Utilization-and-Payment-Data-Phy/fs4p-t5eq.
* Only providers listed as individuals and their services within the 50 states/DC are included.
* Please note that Provider ID is a generated number created by the developer in an effort to de-identify providers.
* Additional data cleaning/transformations on the data set were performed as needed at the sole discretion of the developer.
