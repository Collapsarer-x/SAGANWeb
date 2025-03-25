from flask import Blueprint, jsonify, request
from models import Disease
from sqlalchemy import func

disease_bp = Blueprint('disease_bp', __name__)

class DiseaseAPI:
    @staticmethod
    @disease_bp.route('/api/diseases', methods=['GET'])  # 支持 /api/diseases?id=...
    def get_all_or_by_query():
        disease_query = request.args.get('id')

        if disease_query:
            return DiseaseAPI.get_disease_by_keyword(disease_query)

        diseases = Disease.query.all()
        return jsonify([DiseaseAPI.serialize_disease(d) for d in diseases])

    @staticmethod
    @disease_bp.route('/api/diseases/<string:keyword>', methods=['GET'])  # 支持 /api/diseases/DOID:0001816
    def get_disease_by_path(keyword):
        return DiseaseAPI.get_disease_by_keyword(keyword)

    @staticmethod
    def get_disease_by_keyword(keyword):
        # 优先按 id 精确查找
        disease = Disease.query.get(keyword)
        if disease:
            return jsonify(DiseaseAPI.serialize_disease(disease))

        # 再按 name 精确匹配（不区分大小写）
        disease = Disease.query.filter(func.lower(Disease.name) == keyword.lower()).first()
        if disease:
            return jsonify(DiseaseAPI.serialize_disease(disease))

        return jsonify({'error': 'Disease not found'}), 404

    @staticmethod
    def serialize_disease(disease):
        return {
            "id": disease.id,
            "link": disease.link,
            "name": disease.name,
            "description": disease.description,
            "dbXRefs": disease.dbXRefs,
            "parents": disease.parents,
            "obsoleteTerms": disease.obsoleteTerms,
            "obsoleteXRefs": disease.obsoleteXRefs,
            "children": disease.children,
            "ancestors": disease.ancestors,
            "therapeuticAreas": disease.therapeuticAreas,
            "descendants": disease.descendants,
            "ontology": disease.ontology,
            "synonyms_hasExactSynonym": disease.synonyms_hasExactSynonym,
            "synonyms_hasRelatedSynonym": disease.synonyms_hasRelatedSynonym,
            "synonyms_hasNarrowSynonym": disease.synonyms_hasNarrowSynonym,
            "synonyms_hasBroadSynonym": disease.synonyms_hasBroadSynonym
        }
