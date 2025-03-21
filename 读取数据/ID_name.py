import pandas as pd
import requests
import time

# 读取表格
file_path = "./Fdataset_csv_output/drug_disease_ID.csv"  # 修改为你的文件路径
df = pd.read_csv(file_path)

# 1. 查询 DrugBank ID -> 药物名称（使用 PubChem）
def get_drug_name(drugbank_id):
    """使用 PubChem 查询 DrugBank ID 对应的药物名称"""
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sourceid/DrugBank/{drugbank_id}/JSON"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        name = data["PC_Substances"][0]["substance"]["name"]
        return name
        print(name)
    except Exception:
        return drugbank_id  # 查询失败返回原ID

# 2. 查询 Disease ID -> 疾病名称（使用 NCBI）
def get_disease_name(omim_id):
    """使用 NCBI eUtils API 查询 Disease ID 对应的疾病名称"""
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=omim&id={omim_id}&retmode=json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["result"][omim_id]["title"]
    except Exception:
        return omim_id  # 查询失败返回原ID

# 处理 DrugBank ID -> 药物名称
df["DrugID"] = df["DrugID"].apply(get_drug_name)

# 处理 Disease ID -> 疾病名称
for col in df.columns[2:]:  # 只处理疾病列
    df[col] = df[col].apply(lambda x: get_disease_name(x[1:]) if isinstance(x, str) and x.startswith("D") else x)

# 保存转换后的表格
df.to_csv("drug_disease_name.csv", index=False)
print("转换完成，已保存为 drug_disease_name.csv")
