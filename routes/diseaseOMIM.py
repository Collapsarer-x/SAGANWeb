from flask import Blueprint, jsonify, request
from models import DiseaseOMIM

disease_omim_bp = Blueprint('disease_omim_bp', __name__)

class DiseaseOMIMAPI:
    @staticmethod
    @disease_omim_bp.route('/api/disease_omim', methods=['GET'])
    def get_all_or_by_query():
        record_id = request.args.get('id')
        if record_id:
            return DiseaseOMIMAPI.get_record_by_id(record_id)
        else:
            records = DiseaseOMIM.query.all()
            return jsonify([
                {
                    'ID': r.ID,
                    'Prefix': r.Prefix,
                    'Title': r.Title,
                    'HGNC': r.HGNC,
                    'EnsemblGeneID': r.EnsemblGeneID,
                    'GeneSymbols': r.GeneSymbols,
                    'GeneName': r.GeneName,
                    'RelatedGene': r.RelatedGene,
                    'RelatedGeneMIM': r.RelatedGeneMIM,
                    'DiseaseName': r.DiseaseName
                } for r in records
            ])

    @staticmethod
    @disease_omim_bp.route('/api/disease_omim/<int:record_id>', methods=['GET'])
    def get_record_by_path(record_id):
        return DiseaseOMIMAPI.get_record_by_id(record_id)

    @staticmethod
    def get_record_by_id(record_id):
        record = DiseaseOMIM.query.get(record_id)
        if not record:
            return jsonify({'error': 'DiseaseOMIM record not found'}), 404

        return jsonify({
            'ID': record.ID,
            'Prefix': record.Prefix,
            'Title': record.Title,
            'HGNC': record.HGNC,
            'EnsemblGeneID': record.EnsemblGeneID,
            'GeneSymbols': record.GeneSymbols,
            'GeneName': record.GeneName,
            'RelatedGene': record.RelatedGene,
            'RelatedGeneMIM': record.RelatedGeneMIM,
            'DiseaseName': record.DiseaseName
        })
