from flask import Blueprint, jsonify, request
from models import Drug
from sqlalchemy import func

drug_bp = Blueprint('drug_bp', __name__)

class DrugAPI:
    @staticmethod
    @drug_bp.route('/api/drugs', methods=['GET'])  # 支持 /api/drugs?id=...
    def get_all_or_by_query():
        drug_query = request.args.get('id')

        if drug_query:
            return DrugAPI.get_drug_by_keyword(drug_query)

        drugs = Drug.query.all()
        return jsonify([DrugAPI.serialize_drug(d) for d in drugs])

    @staticmethod
    @drug_bp.route('/api/drugs/<string:keyword>', methods=['GET'])  # 支持 /api/drugs/Cyclizine
    def get_drug_by_path(keyword):
        return DrugAPI.get_drug_by_keyword(keyword)

    @staticmethod
    def get_drug_by_keyword(keyword):
        # 优先按 DrugBank_ID 精确查找
        drug = Drug.query.get(keyword)
        if drug:
            return jsonify(DrugAPI.serialize_drug(drug))

        # 再按 name 精确匹配（不区分大小写）
        drug = Drug.query.filter(func.lower(Drug.name) == keyword.lower()).first()
        if drug:
            return jsonify(DrugAPI.serialize_drug(drug))

        return jsonify({'error': 'Drug not found'}), 404

    @staticmethod
    def serialize_drug(drug):
        return {
            "DrugBank_ID": drug.DrugBank_ID,
            "name": drug.name,
            "type": drug.type,
            "protein_structure": drug.protein_structure,
            "Protein_Chemical_Formula": drug.Protein_Chemical_Formula,
            "Protein_Average_Weight": drug.Protein_Average_Weight,
            "sequences": drug.sequences,
            "pathways": drug.pathways,
            "SMILES": drug.SMILES,
            "target_id": drug.target_id,
            "target_name": drug.target_name,
            "description": drug.description,
            "CAS_Number": drug.CAS_Number,
            "Drug_Groups": drug.Drug_Groups,
            "InChIKey": drug.InChIKey,
            "InChI": drug.InChI,
            "protein_structure2": drug.protein_structure2
        }
