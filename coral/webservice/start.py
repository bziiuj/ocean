import time
import json
from flask import Flask
from flask import request, redirect, Response, url_for
from cryptography import Cryptography
from core_connector import CoreConnector
app = Flask(__name__)
crypto = None


@app.route('/')
def index():
    return redirect(url_for('about'))


@app.route('/about')
def about():
    return '<h1>Hello!</h1><p>You have already accessed the Coral webservice.</p>'


# @app.route('/test_connector', methods=['POST'])
# def test_connector():
#     request_data = request.get_json()
#     final_response = CoreConnector().process_request(request_data)
#     return Response(json.dumps(final_response), mimetype='application/json')


# Webservice methods

@app.route('/handshake', methods=['POST'])
def handshake():
    final_response = {
        'client_id': crypto.register_client_key('582ec7ba-bcf7-45f0-ac1e-ca7c5be136e3')
    }
    return Response(json.dumps(final_response), mimetype='application/json')


@app.route('/sign_in', methods=['POST'])
def sign_in():
    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']
    client_id = request_data['client_id']

    # TODO: implementation

    response_data = True

    final_response = {'status': response_data}
    return Response(json.dumps(final_response), mimetype='application/json')


@app.route('/sign_out', methods=['POST'])
def sign_out():
    request_data = request.get_json()
    client_id = request_data['client_id']

    # TODO: implementation

    response_data = True

    final_response = {'status': response_data}
    return Response(json.dumps(final_response), mimetype='application/json')


@app.route('/get_article_list', methods=['POST'])
def get_article_list():
    request_data = request.get_json()
    last_news_id = request_data['last_news_id']
    count = request_data['count']
    feed_id = request_data['feed_id']
    client_id = request_data['client_id']

    # TODO: implementation

    response_data = []
    for i in range(0, count):
        response_data.append({
            'article_id': '974eeacc-87{0}a-11e3-9f3a-2cd05ae1c39b'.format(i % 10),
            'author': 'Autor {0}'.format(i),
            'title': 'Naglowek {0}'.format(i),
            'time': 1397664087,
            'description': 'Opis {0}'.format(i),
            'image_source': 'http://icons.iconarchive.com/icons/designcontest'
                            '/ecommerce-business/256/news-icon.png'
        })

    final_response = {'article_list': response_data}
    return Response(json.dumps(final_response), mimetype='application/json')


@app.route('/get_article_details', methods=['POST'])
def get_article_details():
    request_data = request.get_json()
    article_id = request_data['article_id']
    client_id = request_data['client_id']

    # TODO: implementation

    response_data = {
        'article_id': '974eeacc-873a-11e3-9f3a-2cd05ae1c39b',
        'body': 'Tekst 7',
    }

    final_response = {'article_details': response_data}
    return Response(json.dumps(final_response), mimetype='application/json')


@app.route('/get_feed_list', methods=['POST'])
def get_feed_list():
    request_data = request.get_json()
    client_id = request_data['client_id']

    final_request = {
        'coralMethodName': 'getFeedList',
        'data': {
            'clientId': client_id
        }
    }

    response_data = CoreConnector().process_request(final_request)

    final_response = {'feed_list': response_data}
    return Response(json.dumps(final_response), mimetype='application/json')


@app.route('/create_feed', methods=['POST'])
def create_feed():
    request_data = request.get_json()
    feed_tags = request_data['feed_tags']
    client_id = request_data['client_id']

    # TODO: implementation

    response_data = True

    final_response = {'status': response_data}
    return Response(json.dumps(final_response), mimetype='application/json')


if __name__ == '__main__':
    # if not crypto:
    #     crypto = Cryptography()

    app.debug = True
    app.run(host='0.0.0.0', port=14)
