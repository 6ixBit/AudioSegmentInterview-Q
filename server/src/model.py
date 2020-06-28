from . import db

from datetime import datetime
from flask import jsonify

class Segments(db.Model):
    id          = db.Column(db.Integer(), primary_key=True)
    name        = db.Column(db.String(50), nullable=False)
    audioStart  = db.Column(db.DateTime(), nullable=False)
    audioEnd    = db.Column(db.DateTime(), nullable=False)

    def __init__(self, name, audioStart, audioEnd):
        self.name       = name
        self.audioStart = audioStart
        self.audioEnd   = audioEnd 

    def __repr__(self):
        return f'{self.name} - {self.audioStart} - {self.audioEnd}'

def getAudioSegments():
    try:
        # Query data
        res = Segments.query.all()
        return res
    except:
        return jsonify({'Error':'Failed to fetch and serialise data.'})

def getAudioSegment(name: str):
    try:
        res = Segments.query.filter_by(name=name)
        return res
    except:
        return jsonify({'Error':'Failed to fetch and serialise data.'})



