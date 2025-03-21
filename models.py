from extension import db

from extension import db  # 确保你从 extension.py 中导入了 db

# 药物表
class Drug(db.Model):
    __tablename__ = 'drug'

    DrugBank_ID = db.Column(db.Text, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    type = db.Column(db.Text)
    protein_structure = db.Column(db.Text)
    Protein_Chemical_Formula = db.Column('Protein Chemical Formula', db.Text)
    Protein_Average_Weight = db.Column('Protein Average Weight', db.Float)
    sequences = db.Column(db.Text)
    pathways = db.Column(db.Text)
    SMILES = db.Column(db.Text)
    target_id = db.Column(db.Text)
    target_name = db.Column(db.Text)
    description = db.Column(db.Text)
    CAS_Number = db.Column('CAS Number', db.Text)
    Drug_Groups = db.Column('Drug Groups', db.Text)
    InChIKey = db.Column(db.Text)
    InChI = db.Column(db.Text)

# 疾病表
class Disease(db.Model):
    __tablename__ = 'disease'

    id = db.Column(db.Text, primary_key=True)  # ⚠️ 数据库中没有主键字段，必须人为指定一个字段作为主键
    code = db.Column(db.Text)
    dbXRefs = db.Column(db.Text)
    description = db.Column(db.Text)
    name = db.Column(db.Text)
    parents = db.Column(db.Text)
    therapeuticAreas = db.Column(db.Text)
    MeSH = db.Column(db.Text)
    OMIM = db.Column(db.Text)

# 文献表
class Literature(db.Model):
    __tablename__ = 'literature'

    # 数据库没有主键字段，必须人为指定一个作为主键
    DrugID = db.Column(db.Text, primary_key=True)  # ⚠️ 可根据实际情况改为更合适的主键字段
    DrugName = db.Column(db.Text)
    PubChemID = db.Column(db.BigInteger)
    Target = db.Column(db.Text)
    Disease = db.Column(db.Text)
    Side_effect = db.Column(db.Text)
    NewDirectTarget = db.Column(db.Text)
    NewIndirectTarget = db.Column(db.Text)
    NewDisease = db.Column(db.Text)
    Evidence = db.Column(db.Text)
    Insilico = db.Column(db.Text)
    Invitro = db.Column(db.Text)
    Invivo = db.Column(db.Text)
    Clinicaltrial = db.Column(db.Text)
    SupportedSentences = db.Column(db.Text)
    PMID = db.Column(db.BigInteger)
