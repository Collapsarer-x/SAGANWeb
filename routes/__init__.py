from routes.drug import drug_bp
from routes.disease import disease_bp
from routes.literature import literature_bp

# 所有蓝图统一收集到一个列表中
all_blueprints = [
    drug_bp,
    disease_bp,
    literature_bp
]
