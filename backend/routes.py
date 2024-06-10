from flask import Blueprint, jsonify
from models import Scholarship

bp = Blueprint('main', __name__)


@bp.route('/all_scholarships', methods=['GET'])
def all_scholarships():
    scholarships = Scholarship.query.all()
    result = [
        {
            'id': scholarship.id,
            'name': scholarship.name,
            'description': scholarship.description,
            'offered_by': scholarship.offered_by,
            'type': scholarship.type,
            'citizenship_type': scholarship.citizenship_type,
            'application_required': scholarship.application_required,
            'nature_of_award': scholarship.nature_of_award,
            'application_deadline': scholarship.application_deadline,
            'value': scholarship.value,
            'university': scholarship.university
        }
        for scholarship in scholarships
    ]
    return jsonify(result)
@bp.route('/test_db')
def test_db():
    scholarships = Scholarship.query.all()
    return jsonify([s.name for s in scholarships])
@bp.route('/test')
def test():
    return jsonify({'message': 'Hello, World!'})