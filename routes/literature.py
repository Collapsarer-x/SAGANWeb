from flask import Blueprint, jsonify, request
from models import Literature
from sqlalchemy import or_

literature_bp = Blueprint('literature_bp', __name__)

class LiteratureAPI:
    @staticmethod
    @literature_bp.route('/api/literatures', methods=['GET'])
    def get_all_or_by_query():
        query = request.args.get('query')

        # ✅ 查询模式：query参数优先匹配 DrugID，其次 DrugName（完全匹配）
        if query:
            return LiteratureAPI.get_literature_by_keyword(query)

        # ✅ 无 query 参数：返回所有数据
        literatures = Literature.query.all()
        return jsonify([
            LiteratureAPI.serialize_literature(l) for l in literatures if l is not None
        ])

    @staticmethod
    @literature_bp.route('/api/literatures/<string:keyword>', methods=['GET'])
    def get_literature_by_path(keyword):
        return LiteratureAPI.get_literature_by_keyword(keyword)

    @staticmethod
    def get_literature_by_keyword(keyword):
        # 先按 DrugID 查找
        literature = Literature.query.filter_by(DrugID=keyword).first()
        if literature:
            return jsonify(LiteratureAPI.serialize_literature(literature))

        # 再按 DrugName 精确匹配（不区分大小写）
        literature = Literature.query.filter(Literature.DrugName.ilike(keyword)).first()
        if literature:
            return jsonify(LiteratureAPI.serialize_literature(literature))

        return jsonify({'error': 'Literature not found'}), 404

    @staticmethod
    def serialize_literature(l):
        return {
            "DrugName": l.DrugName,
            "DrugID": l.DrugID,
            "PubChemID": l.PubChemID,
            "OriginalTarget": l.OriginalTarget,
            "OriginalIndication": l.OriginalIndication,
            "Side_effect": l.Side_effect,
            "RepositionedDirectTarget": l.RepositionedDirectTarget,
            "RepositionedIndirectTarget": l.RepositionedIndirectTarget,
            "RepositionedIndication": l.RepositionedIndication,
            "Evidence": l.Evidence,
            "Insilico": l.Insilico,
            "Invitro": l.Invitro,
            "Invivo": l.Invivo,
            "Clinicaltrial": l.Clinicaltrial,
            "SupportedSentences": l.SupportedSentences,
            "PMID": l.PMID
        }
