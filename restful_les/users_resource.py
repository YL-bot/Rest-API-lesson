from flask_restful import reqparse, abort, Api, Resource
from flask import jsonify
from data.users import User
from data import db_session
import datetime 


def abort_if_users_not_found(user_id):
    session = db_session.create_session()
    
    users = session.query(User).get(user_id)
    
    if not users:
        abort(404, message=f"News {user_id} not found")


parser = reqparse.RequestParser()
parser.add_argument('address', required=True, type=str)
parser.add_argument('email', required=True, type=str)
parser.add_argument('name', required=True, type=str)
parser.add_argument('position', required=True, type=str)
parser.add_argument('surname', required=True, type=str)
parser.add_argument('speciality', required=True, type=str)
parser.add_argument('password_hash', required=True, type=str)
parser.add_argument('age', required=True, type=int)
parser.add_argument('modified_date', required=True, default=datetime.datetime.now())
parser.add_argument('id', required=False, type=int)


class UsersResource(Resource):
    def get(self, user_id):       
        abort_if_users_not_found(user_id)
        
        db_sess = db_session.create_session()
        users = db_sess.query(User).get(user_id)
    
        if not users:
            return jsonify({'error': 'Not found'})
    
        return jsonify({'user': users.to_dict()})
        
        
    def delete(self, user_id):
        abort_if_users_not_found(user_id)
        
        db_sess = db_session.create_session()
    
        try:
            user = db_sess.query(User).get(user_id)
            if not user:
                return jsonify({'error': 'Not found'})
    
            db_sess.delete(user)
            db_sess.commit()
        
            return jsonify({'success': 'OK'})
    
        except Exception:
            return jsonify({'error': 'Bad request'})
    
    
    def put(self, user_id):
        args = parser.parse_args()
        if not args:
            return jsonify({'error': 'Empty request'})
    
        elif not all(key in args for key in ['address', 'age', 'email', 'modified_date', 'name', 'position', 'surname', 'speciality', 'password_hash']):
            return jsonify({'error': 'Bad request'})
    
        db_sess = db_session.create_session()
    
        if args['id']:
            if db_sess.query(User).filter(User.id == user_id).first():
                return jsonify({'error': 'Exception'})
        
        if db_sess.query(User).filter(User.email == args['email']).first():
            return jsonify({'error': 'Email already exists'})
    
        user = db_sess.query(User).filter(User.id == user_id).first()
    
        user.address=args['address'],
        user.age=args['age'],
        user.email=args['email'],
        user.modified_date=args['modified_date'],
        user.name=args['name'],
        user.position=args['position'],
        user.surname=args['surname'],
        user.speciality=args['speciality'],
        user.password_hash=args['password_hash'],
    
        db_sess.commit()
    
        return jsonify({'success': 'OK'})
    
    
    
class UsersListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        users = db_sess.query(User).all()
    
        return jsonify({'users': [item.to_dict() for item in users]})


    def post(self):
        args = parser.parse_args()
        if not args:
            return jsonify({'error': 'Empty request'})
    
        elif not all(key in args for key in ['address', 'age', 'email', 'modified_date', 'name', 'position', 'surname', 'speciality', 'password_hash']):
            return jsonify({'error': 'Bad request'})
    
        db_sess = db_session.create_session()
    
        if args['id']:
            if db_sess.query(User).filter(User.id == args['id']).first():
                return jsonify({'error': ' Id already exists'})
        
        if db_sess.query(User).filter(User.email == args['email']).first():
            return jsonify({'error': 'Email already exists'})
    
        if args['id']:
            user = User(address=args['address'],
                        age=args['age'],
                        email=args['email'],
                        modified_date=args['modified_date'],
                        name=args['name'],
                        position=args['position'],
                        surname=args['surname'],
                        speciality=args['speciality'],
                        password_hash=args['password_hash'],
                        id=args['id']
                        )
        else:
            user = User(address=args['address'],
                        age=args['age'],
                        email=args['email'],
                        modified_date=args['modified_date'],
                        name=args['name'],
                        position=args['position'],
                        surname=args['surname'],
                        speciality=args['speciality'],
                        password_hash=args['password_hash'],
                        )
    

        db_sess.add(user)
        db_sess.commit()
    
        return jsonify({'success': 'OK'})
