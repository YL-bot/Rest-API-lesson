import flask
from flask import request, jsonify
from . import db_session
from .jobs import Jobs
from .users import User


blueprint = flask.Blueprint('users_api', __name__, template_folder='templates')


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    
    return jsonify({'users': [item.to_dict() for item in users]})


@blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def get_1_user(user_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(user_id)
    
    if not users:
        return jsonify({'error': 'Not found'})
    
    return jsonify({'user': users.to_dict()})


#{"user":{"address":"module_1","age":19,"email":"tom_rf@mars.org","id":2,"modified_date":"2023-03-03 12:57:33","name":"Roling",
#         "password_hash":"pbkdf2:sha256:260000$yilawWgMGYQPegQ4$6c1c4ed775ee52c71fa8bd89be8f8a53e28b1ce69edcae316b267f493645961f","position":"trainee","speciality":"doctor","surname":"Tom"}}


@blueprint.route('/api/users', methods=['POST'])
def add_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    
    elif not all(key in request.json for key in ['address', 'age', 'email', 'modified_date', 'name', 'position', 'surname', 'speciality', 'password_hash']):
        return jsonify({'error': 'Bad request'})
    
    db_sess = db_session.create_session()
    
    if 'id' in request.json:
        if db_sess.query(User).filter(User.id == request.json['id']).first():
            return jsonify({'error': ' Id already exists'})
        
    if db_sess.query(User).filter(User.email == request.json['email']).first():
        return jsonify({'error': 'Email already exists'})
    
    if 'id' in request.json:
        user = User(address=request.json['address'],
                    age=request.json['age'],
                    email=request.json['email'],
                    modified_date=request.json['modified_date'],
                    name=request.json['name'],
                    position=request.json['position'],
                    surname=request.json['surname'],
                    speciality=request.json['speciality'],
                    password_hash=request.json['password_hash'],
                    id=request.json['id']
                    )
    else:
        user = User(address=request.json['address'],
                    age=request.json['age'],
                    email=request.json['email'],
                    modified_date=request.json['modified_date'],
                    name=request.json['name'],
                    position=request.json['position'],
                    surname=request.json['surname'],
                    speciality=request.json['speciality'],
                    password_hash=request.json['password_hash'],
                    )
    

    db_sess.add(user)
    db_sess.commit()
    
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
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


@blueprint.route('/api/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    
    elif not all(key in request.json for key in ['address', 'age', 'email', 'modified_date', 'name', 'position', 'surname', 'speciality', 'password_hash']):
        return jsonify({'error': 'Bad request'})
    
    db_sess = db_session.create_session()
    
    if 'id' in request.json:
        if db_sess.query(User).filter(User.id == user_id).first():
            return jsonify({'error': 'Exception'})
        
    if db_sess.query(User).filter(User.email == request.json['email']).first():
        return jsonify({'error': 'Email already exists'})
    
    user = db_sess.query(User).filter(User.id == user_id).first()
    
    user.address=request.json['address'],
    user.age=request.json['age'],
    user.email=request.json['email'],
    user.modified_date=request.json['modified_date'],
    user.name=request.json['name'],
    user.position=request.json['position'],
    user.surname=request.json['surname'],
    user.speciality=request.json['speciality'],
    user.password_hash=request.json['password_hash'],
    
    db_sess.commit()
    
    return jsonify({'success': 'OK'})