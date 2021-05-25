import dash
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from config import Config


app = dash.Dash(__name__)
server_flask = app.server

# configure Flask settings
server_flask.config.from_object(Config)

# set up caching; (cache configuration settings in config file)
cache = Cache(server_flask)

db = SQLAlchemy(server_flask)


# this import is a workaround to circular imports in Flask since other modules need to import the app variable defined above
from app import models, layout, interactivity, excel_export