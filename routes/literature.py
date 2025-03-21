from flask import Blueprint, jsonify, request
from models import Literature

literature_bp = Blueprint('literature_bp', __name__)

class LiteratureAPI:
    @staticmethod
    @literature_bp.route('/api/literatures', methods=['GET'])
    def get_all_or_by_query():
        literature_id = request.args.get('id')
        if literature_id:
            return LiteratureAPI.get_literature_by_id(literature_id)
        else:
            literatures = Literature.query.all()
            return jsonify([
                {
                    "DrugID": l.DrugID,
                    "DrugName": l.DrugName,
                    "PubChemID": l.PubChemID,
                    "Target": l.Target,
                    "Disease": l.Disease,
                    "Side_effect": l.Side_effect,
                    "NewDirectTarget": l.NewDirectTarget,
                    "NewIndirectTarget": l.NewIndirectTarget,
                    "NewDisease": l.NewDisease,
                    "Evidence": l.Evidence,
                    "Insilico": l.Insilico,
                    "Invitro": l.Invitro,
                    "Invivo": l.Invivo,
                    "Clinicaltrial": l.Clinicaltrial,
                    "SupportedSentences": l.SupportedSentences,
                    "PMID": l.PMID
                } for l in literatures
            ])

    @staticmethod
    @literature_bp.route('/api/literatures/<string:literature_id>', methods=['GET'])
    def get_literature_by_path(literature_id):
        return LiteratureAPI.get_literature_by_id(literature_id)

    @staticmethod
    def get_literature_by_id(literature_id):
        literature = Literature.query.get(literature_id)
        if not literature:
            return jsonify({'error': 'Literature not found'}), 404

        return jsonify({
            "DrugID": literature.DrugID,
            "DrugName": literature.DrugName,
            "PubChemID": literature.PubChemID,
            "Target": literature.Target,
            "Disease": literature.Disease,
            "Side_effect": literature.Side_effect,
            "NewDirectTarget": literature.NewDirectTarget,
            "NewIndirectTarget": literature.NewIndirectTarget,
            "NewDisease": literature.NewDisease,
            "Evidence": literature.Evidence,
            "Insilico": literature.Insilico,
            "Invitro": literature.Invitro,
            "Invivo": literature.Invivo,
            "Clinicaltrial": literature.Clinicaltrial,
            "SupportedSentences": literature.SupportedSentences,
            "PMID": literature.PMID
        })
