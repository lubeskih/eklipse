from flask import Flask, jsonify
from flask import render_template
from werkzeug.exceptions import InternalServerError, BadRequest

from eklipse.utils.json_serializer import AlchemyEncoder
from .models import SolarEclipse

app = Flask(__name__, instance_relative_config=True, static_url_path='/static')

app.config.from_object('config')
app.config.from_pyfile('config.py')
app.json_encoder = AlchemyEncoder

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(app.config['DATABASE_URL'], convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/query/<string:geoArea>')
def getAreaByInput(geoArea):
    """
    :return: Returns specific geoloc in JSON Format
    :rtype: json
    """
    try:
        data = db_session.query(SolarEclipse).filter_by(
            geoArea=geoArea.title()).all()
    except InternalServerError:
        return jsonify({'data': "Internal server error", 'status': 'success'})

    if not data:
        return jsonify({'data': "No data found", 'status': 'success'})

    return jsonify({'data': data, 'status': 'success'})