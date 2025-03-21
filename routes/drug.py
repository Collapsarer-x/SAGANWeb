from flask import Blueprint, jsonify, request
from models import Drug

drug_bp = Blueprint('drug_bp', __name__)

class DrugAPI:
    # 装饰器, 不需要访问类的实例或类本身
    @staticmethod
    @drug_bp.route('/api/drugs', methods=['GET'])  # 支持 /api/drugs?id=...
    def get_all_or_by_query():
        drug_id = request.args.get('id')
        if drug_id:
            return DrugAPI.get_drug_by_id(drug_id)
        else:
            drugs = Drug.query.all()
            return jsonify([
                {
                    "DrugBank_ID": d.DrugBank_ID,
                    "name": d.name,
                    "type": d.type,
                    "protein_structure": d.protein_structure,
                    "Protein_Chemical_Formula": d.Protein_Chemical_Formula,
                    "Protein_Average_Weight": d.Protein_Average_Weight,
                    "sequences": d.sequences,
                    "pathways": d.pathways,
                    "SMILES": d.SMILES,
                    "target_id": d.target_id,
                    "target_name": d.target_name,
                    "description": d.description,
                    "CAS_Number": d.CAS_Number,
                    "Drug_Groups": d.Drug_Groups,
                    "InChIKey": d.InChIKey,
                    "InChI": d.InChI
                } for d in drugs
            ])

    @staticmethod
    @drug_bp.route('/api/drugs/<string:drug_id>', methods=['GET'])  # 支持 /api/drugs/DB00001
    def get_drug_by_path(drug_id):
        return DrugAPI.get_drug_by_id(drug_id)

    @staticmethod
    def get_drug_by_id(drug_id):
        drug = Drug.query.get(drug_id)
        if not drug:
            return jsonify({'error': 'Drug not found'}), 404
        return jsonify({
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
            "InChI": drug.InChI
        })
