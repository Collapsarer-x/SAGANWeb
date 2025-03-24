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
    protein_structure2 = db.Column(db.Text)

# 疾病表_EFO
class DiseaseEFO(db.Model):
    __tablename__ = 'disease_EFO'

    id = db.Column(db.Text, primary_key=True)  # ⚠️ 数据库中没有主键字段，必须人为指定一个字段作为主键
    code = db.Column(db.Text)
    dbXRefs = db.Column(db.Text)
    description = db.Column(db.Text)
    name = db.Column(db.Text)
    parents = db.Column(db.Text)
    therapeuticAreas = db.Column(db.Text)
    MeSH = db.Column(db.Text)
    OMIM = db.Column(db.Text)

# 疾病表_omim
class DiseaseOMIM(db.Model):
    __tablename__ = 'disease_omim'

    ID = db.Column(db.BigInteger, primary_key=True)  # 如果不是主键，可改为 nullable=True
    Prefix = db.Column(db.Text)
    Title = db.Column(db.Text)
    HGNC = db.Column(db.Text)
    EnsemblGeneID = db.Column(db.Text)
    GeneSymbols = db.Column(db.Text)
    GeneName = db.Column(db.Text)
    RelatedGene = db.Column(db.Text)
    RelatedGeneMIM = db.Column(db.Text)
    DiseaseName = db.Column(db.Text)



# 文献表
class Literature(db.Model):
    __tablename__ = 'literature'

    DrugName = db.Column(db.Text)
    DrugID = db.Column(db.Text, primary_key=True)
    PubChemID = db.Column(db.Integer)
    OriginalTarget = db.Column(db.Text)
    OriginalIndication = db.Column(db.Text)
    Side_effect = db.Column(db.Text)
    RepositionedDirectTarget = db.Column(db.Text)
    RepositionedIndirectTarget = db.Column(db.Text)
    RepositionedIndication = db.Column(db.Text)
    Evidence = db.Column(db.Text)
    Insilico = db.Column(db.Text)
    Invitro = db.Column(db.Text)
    Invivo = db.Column(db.Text)
    Clinicaltrial = db.Column(db.Text)
    SupportedSentences = db.Column(db.Text)
    PMID = db.Column(db.Integer)