import flask
from flask import request, jsonify
from . import db_session
from .jobs import Jobs
from .users import User


blueprint = flask.Blueprint('jobs_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    
    
    return jsonify({'jobs': [item.to_dict() for item in jobs]})


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_1_job(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(job_id)
    
    if not jobs:
        return jsonify({'error': 'Not found'})
    
    return jsonify({'job': jobs.to_dict()})


#{"job":{"collaborators":"2, 3","end_date":"2023-03-03 12:58:30","id":2,"is_finished":false,"job":"deployment of residential modules 1 and 2",
# "start_date":"2023-03-03 12:58:30","team_leader":1,"work_size":15}}

@blueprint.route('/api/jobs', methods=['POST'])
def add_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    
    elif not all(key in request.json for key in ['team_leader', 'title', 'work_size', 'collaborators', 'is_finished', 'start_date', 'end_date']):
        return jsonify({'error': 'Bad request'})
    
    db_sess = db_session.create_session()
    
    if 'id' in request.json:
        if db_sess.query(Jobs).filter(Jobs.id == request.json['id']).first():
            return jsonify({'error': ' Id already exists'})
        
    if not db_sess.query(User).filter(User.id == request.json['team_leader']).first():
        return jsonify({'error': 'Bad request'})
    
    if 'id' in request.json:
        job = Jobs(job=request.json['title'],
                    team_leader=request.json['team_leader'],
                    work_size=request.json['work_size'],
                    collaborators=request.json['collaborators'],
                    start_date=request.json['start_date'],
                    end_date=request.json['end_date'],
                    is_finished=request.json['is_finished'],
                    id=request.json['id']
                    )
    else:
        job = Jobs(job=request.json['title'],
                    team_leader=request.json['team_leader'],
                    work_size=request.json['work_size'],
                    collaborators=request.json['collaborators'],
                    start_date=request.json['start_date'],
                    end_date=request.json['end_date'],
                    is_finished=request.json['is_finished'],
                    )
    

    db_sess.add(job)
    db_sess.commit()
    
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    db_sess = db_session.create_session()
    
    try:
        job = db_sess.query(Jobs).get(job_id)
        if not job:
            return jsonify({'error': 'Not found'})
    
        db_sess.delete(job)
        db_sess.commit()
        
        return jsonify({'success': 'OK'})
    
    except Exception:
        return jsonify({'error': 'Bad request'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['PUT'])
def edit_job(job_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    
    elif not all(key in request.json for key in ['team_leader', 'title', 'work_size', 'collaborators', 'is_finished', 'start_date', 'end_date']):
        return jsonify({'error': 'Bad request'})
    
    db_sess = db_session.create_session()
    
    if 'id' in request.json:
        if db_sess.query(Jobs).filter(Jobs.id == job_id).first():
            return jsonify({'error': 'Exception'})
        
    if not db_sess.query(User).filter(User.id == request.json['team_leader']).first():
        return jsonify({'error': 'Bad request'})
    
    job = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
    
    job.team_leader = request.json['team_leader']
    job.job = request.json['title']
    job.work_size = request.json['work_size']
    job.collaborators = request.json['collaborators']
    job.start_date = request.json['start_date']
    job.end_date = request.json['end_date']
    job.is_finished = request.json['is_finished']
    
    db_sess.commit()
    
    return jsonify({'success': 'OK'})