from api.models import db,Request
from api.shared.utils import HTTPStatus,RequestStatus

class Requests_service():
    @staticmethod
    def create_request(data, client_id):
        new_request = Request(body=data['body'], status=RequestStatus.Pending.value, created_by=client_id)
        db.session.add(new_request)
        db.session.commit()
        return {'message': 'Request created successfully'}, HTTPStatus.CREATED
    
    @staticmethod
    def get_requests():
        requests = Request.query.all()
        result = [{'id': request.id, 'body': request.body, 'status': request.status, 'processed_by': request.processed_by} for request in requests]
        return result, HTTPStatus.OK

    @staticmethod
    def update_request(id, data):
        request = Request.query.get(id)
        if request:
            request.body = data.get('body', request.body)
            db.session.commit()
            return {'message': 'Request updated successfully'}, HTTPStatus.OK
        else:
            return {'error': 'Request not found'}, HTTPStatus.NOT_FOUND

    @staticmethod
    def delete_request(id):
        request = Request.query.get(id)
        if request:
            db.session.delete(request)
            db.session.commit()
            return {'message': 'Request deleted successfully'}, HTTPStatus.NO_CONTENT
        else:
            return {'error': 'Request not found'}, HTTPStatus.NOT_FOUND
        
    @staticmethod
    def update_request_status(id, data, operator_id):
        request = Request.query.get(id)
        if request:
            request.status = data.get('status', request.status)
            request.processed_by = operator_id
            db.session.commit()
            return {'message': 'Request status updated successfully'}, HTTPStatus.OK
        else:
            return {'error': 'Request not found'}, HTTPStatus.NOT_FOUND