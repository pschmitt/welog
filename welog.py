#!/usr/bin/env python
# coding: utf-8


import os
from logging.config import dictConfig

from flask import Flask, request


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


HTTP_METHODS = [
    'GET',
    'HEAD',
    'POST',
    'DELETE',
    'PUT',
    'PATCH',
    'OPTIONS'
]


app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=HTTP_METHODS)
def log_all(path):
    app.logger.info('%s %s', request.method, request.url)
    app.logger.info('Headers:\n%s', request.headers)
    app.logger.info('URL Args: %s', dict(request.args))
    app.logger.info('Form data: %s', dict(request.form))
    app.logger.info('JSON Data: %s', request.json)
    app.logger.info('Body: %s', request.data)
    return os.environ.get('HTTP_RESPONSE_BODY', 'OK')


if __name__ == '__main__':
    DEBUG = os.environ.get('FLASK_DEBUG', '0') == '1'
    app.run(debug=DEBUG, host='0.0.0.0')
