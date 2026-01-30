import common
from flask import request

@common.app.route('/api/test', methods=['GET', 'POST'])
def _api_test():
    match request.method:
        case 'GET':  return test_get()
        case 'POST': return test_post()

def test_get():
    return { 'test': 'get' }

def test_post():
    return { 'test': 'post' }
