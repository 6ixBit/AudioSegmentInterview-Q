# Contains logic to return JSON data to endpoints
from .model import Segments, getAudioSegment, getAudioSegments

from flask import jsonify
from datetime import date, timedelta
import datetime

def calcNumbOfTimesTalked():
    resp = getAudioSegments()

    timesTalked = {}

    for audio in resp:
        if audio.name in timesTalked:
            timesTalked[audio.name] += 1
        else:
            timesTalked[audio.name] = 1

    return jsonify(timesTalked)

def calcContributionToCall():
    resp = getAudioSegments()

    audioContribution = {}
    for audio in resp:
        duration = substractTimeDuration(audio.audioStart, audio.audioEnd)

        if audio.name in audioContribution:
            audioContribution[audio.name] += duration
        else:
            audioContribution[audio.name] = duration
    return jsonify(audioContribution)

def calcAllStats():
    resp = getAudioSegments()

    resObject = {}
    # Generate amount of times a participant talked and total duration in seconds
    for audio in resp:
        duration = substractTimeDuration(audio.audioStart, audio.audioEnd)

        if audio.name in resObject:
            resObject[audio.name]["timesTalked"] += 1
            resObject[audio.name]["callContributions"] += duration
        else:
             obj = {
                 audio.name: {
                     "timesTalked": 1,
                     "callContributions": duration
                 }
             }
             resObject.update(obj)

    # Calc Average
    for _, v in resObject.items():
        v['avgCallContributions'] = calcAvg(v['callContributions'], v['timesTalked'])
    return jsonify(resObject)
        
# Helpers
def substractTimeDuration(start, end):
    start = timedelta(minutes=start.minute, seconds=start.second) 
    end = timedelta(minutes=end.minute, seconds=end.second)

    output = start-end
    return abs(output.total_seconds())

def calcAvg(duration, count):
    return round(duration / count, 2)

