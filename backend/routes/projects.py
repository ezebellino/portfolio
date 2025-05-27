# backend/routes/projects.py
from flask import Blueprint, jsonify
from models.project import Project

projects_bp = Blueprint('projects', __name__, url_prefix='/api')

@projects_bp.route('/projects')
def get_projects():
    projects = Project.query.all()
    return jsonify([p.serialize() for p in projects])
