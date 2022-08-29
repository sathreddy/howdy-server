from flask import Flask

api = Flask(__name__)

@api.route('/listings')
def get_listings():
    response_body = {
        'message': 'Hello, World!'
    }
    return response_body