from functools import wraps
from flask import request, jsonify
from http import HTTPStatus


def validate_is_enum(field_name, enum_class):
    enum_values = {e.value for e in enum_class}

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            data = request.json
            if field_name not in data:
                return jsonify({'error': f'Missing {field_name} field'}), HTTPStatus.BAD_REQUEST
            if data[field_name] not in enum_values:
                return jsonify({'error': f'Invalid {field_name} value'}), HTTPStatus.BAD_REQUEST
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def is_string_length(field, min_length, max_length):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            data = request.json
            if field not in data:
                return jsonify({'error': f'Missing {field} field'}), HTTPStatus.BAD_REQUEST
            value = data[field]
            if not isinstance(value, str):
                return jsonify({'error': f'{field} must be a string'}), HTTPStatus.BAD_REQUEST
            if len(value) < min_length or len(value) > max_length:
                return jsonify({'error': f'{field} length must be between {min_length} and {max_length}'}), HTTPStatus.BAD_REQUEST
            return f(*args, **kwargs)
        return decorated_function
    return decorator