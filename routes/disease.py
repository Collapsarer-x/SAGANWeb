from flask import Blueprint, jsonify, request
from models import Disease

disease_bp = Blueprint('disease_bp', __name__)

class DiseaseAPI:
    @staticmethod
    @disease_bp.route('/api/diseases', methods=['GET'])
    def get_all_or_by_query():
        disease_id = request.args.get('id')
        if disease_id:
            return DiseaseAPI.get_disease_by_id(disease_id)
        else:
            diseases = Disease.query.all()
            return jsonify([
                {
                    'id': d.id,
                    'code': d.code,
                    'name': d.name,
                    'description': d.description,
                    'dbXRefs': d.dbXRefs,
                    'parents': d.parents,
                    'therapeuticAreas': d.therapeuticAreas,
                    'MeSH': d.MeSH,
                    'OMIM': d.OMIM
                } for d in diseases
            ])

    @staticmethod
    @disease_bp.route('/api/diseases/<string:disease_id>', methods=['GET'])
    def get_disease_by_path(disease_id):
        return DiseaseAPI.get_disease_by_id(disease_id)

    @staticmethod
    def get_disease_by_id(disease_id):
        disease = Disease.query.get(disease_id)
        if not disease:
            return jsonify({'error': 'Disease not found'}), 404

        return jsonify({
            'id': disease.id,
            'code': disease.code,
            'name': disease.name,
            'description': disease.description,
            'dbXRefs': disease.dbXRefs,
            'parents': disease.parents,
            'therapeuticAreas': disease.therapeuticAreas,
            'MeSH': disease.MeSH,
            'OMIM': disease.OMIM
        })
