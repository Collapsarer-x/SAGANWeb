from flask import Blueprint, jsonify, request
from models import DiseaseEFO

disease_EFO_bp = Blueprint('disease_bp', __name__)

class DiseaseAPI:
    @staticmethod
    @disease_EFO_bp.route('/api/diseases_EFO', methods=['GET'])
    def get_all_or_by_query():
        disease_id = request.args.get('id')
        if disease_id:
            return DiseaseAPI.get_disease_by_id(disease_id)
        else:
            diseases = DiseaseEFO.query.all()
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
    @disease_EFO_bp.route('/api/diseases_EFO/<string:disease_id>', methods=['GET'])
    def get_disease_by_path(disease_id):
        return DiseaseAPI.get_disease_by_id(disease_id)

    @staticmethod
    def get_disease_by_id(disease_id):
        disease = DiseaseEFO.query.get(disease_id)
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
