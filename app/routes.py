from app import app

import wrdl_grabber.grabber as grbr

@app.route('/')
@app.route('/index/')
def index():

    return "Welcome to the Wordle Catch-Up API!\nWritten by Perry Oddo and Callum Wayman"

@app.route('/word/', methods=['GET'])
@app.route('/word/<date>', methods=['GET'])
def get_word(date='01/10/2022'):

    return grbr.fetch_word(date)
