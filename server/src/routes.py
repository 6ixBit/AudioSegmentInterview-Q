from .controller import calcNumbOfTimesTalked, calcContributionToCall, calcAllStats

from . import app

@app.route("/stat/timestalked", methods=['GET'])
def status():
    resp = calcNumbOfTimesTalked()
    return resp 

@app.route("/stat/callcontribution", methods=['GET'])
def stat():
    resp = calcContributionToCall() 
    return resp

@app.route("/stat/all", methods=['GET'])
def allStats():
    resp = calcAllStats()
    return resp