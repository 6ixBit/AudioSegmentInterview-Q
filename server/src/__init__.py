from config import Config

# Third party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initialize
app = Flask(__name__) 
app.config.from_object(Config)
db = SQLAlchemy(app)
CORS(app)

# Import additional files to Flask can recognise them
from . import routes, model, controller