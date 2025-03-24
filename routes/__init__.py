from routes.drug import drug_bp
from routes.diseaseEFO import disease_EFO_bp
from routes.literature import literature_bp
from routes.diseaseOMIM import disease_omim_bp

# 所有蓝图统一收集到一个列表中
all_blueprints = [
    drug_bp,
    disease_EFO_bp,
    disease_omim_bp,
    literature_bp
]
