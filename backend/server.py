import testpilot
import sys

from flask import Flask, jsonify

app = Flask(__name__)


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