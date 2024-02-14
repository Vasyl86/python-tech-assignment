from functools import wraps
from http import HTTPStatus
from flask import request, jsonify

def operator_guard(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'Operator-ID' not in request.headers:
            return jsonify({'error': 'Authentication header is missing'}), HTTPStatus.UNAUTHORIZED.value
        
        return f(*args, **kwargs)
    
    return decorated_function