import testpilot
import sys
from random import randint
from flask import Flask, jsonify, render_template, send_file


import sys
sys.path.insert(0, "C:\\Users\\dyako\\Documents\\CandyRobot\\picture")
import picture

app = Flask(__name__)


@app.route('/base')
def static_page():
    return render_template('base.html')

@app.route('/controlpanel')
def controlpanel():
    return render_template('controlpanel.html')

@app.route('/createphoto', methods=['GET'])
def createphoto():
    picture.start()
    return 'wait a second'

@app.route('/qr_url')
def qr_url():
    return send_file('qr.png', mimetype='image/png')

@app.route('/get_random')
def get_random():
    testpilot.gotobasket(randint(0, 3))
    time.sleep(10)
    testpilot.getcandies()
    time.sleep(10)
    testpilot.abortcandies()
    return 'ok'

@app.route('/get_image')
def get_image():
    get_random()
    return send_file('mymosaic.jpg', mimetype='image/jpg')

@app.route('/test', methods=['GET'])
def get_tasks():
    return 'test'

@app.route('/gotobasket/<int:basket_id>', methods=['GET'])
def gotobaskets(basket_id):
    testpilot.gotobasket(basket_id)
    return 'ok'

@app.route('/getcandies', methods=['GET'])
def getcandies():
    testpilot.getcandies()
    return 'ok'

@app.route('/fakecandies', methods=['GET'])
def fakecandies():
    testpilot.fakecandies()
    return 'ok'

@app.route('/abortcandies', methods=['GET'])
def abortcandies():
    testpilot.abortcandies()
    return 'ok'

@app.route('/goodbye', methods=['GET'])
def goodbye():
    testpilot.goodbye()
    return 'ok'

@app.route('/')
def index():
    testpilot.connect()
    return "connected and calibrated"

'''
@app.before_first_request
def startup():
    print()
'''
if __name__ == '__main__':
    app.run(debug=True)