from http import HTTPStatus
from api.models import db,Client

class Clients_service:
    @staticmethod
    def create_client(data):
        new_client = Client(first_name=data['first_name'], last_name=data['last_name'], phone=data['phone'])
        db.session.add(new_client)
        db.session.commit()
        return {'message': 'Client created successfully'}, HTTPStatus.CREATED
    
    @staticmethod
    def get_clients():
        clients = Client.query.all()
        result = [{'id': client.id, 'first_name': client.first_name, 'last_name': client.last_name, 'phone': client.phone} for client in clients]
        return result, HTTPStatus.OK

    @staticmethod
    def update_client(id, data):
        client = Client.query.get(id)
        if client:
            client.first_name = data.get('first_name', client.first_name)
            client.last_name = data.get('last_name', client.last_name)
            client.phone = data.get('phone', client.phone)
            db.session.commit()
            return {'message': 'Client updated successfully'}, HTTPStatus.OK
        else:
            return {'error': 'Client not found'}, HTTPStatus.NOT_FOUND

    @staticmethod
    def delete_client(id):
        client = Client.query.get(id)
        if client:
            db.session.delete(client)
            db.session.commit()
            return {'message': 'Client deleted successfully'}, HTTPStatus.NO_CONTENT
        else:
            return {'error': 'Client not found'}, HTTPStatus.NOT_FOUND
        