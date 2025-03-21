import pandas as pd


def parse_id_file(content):
    return [line.strip("[]'\n ") for line in content.split('\n') if line.strip()]


# 读取映射文件
with open('./Cdataset_csv_output/Wdname.csv', 'r') as f:
    disease_ids = parse_id_file(f.read())[1:]  # 跳过首行0

with open('./Cdataset_csv_output/Wrname.csv', 'r') as f:
    drug_ids = parse_id_file(f.read())[1:]  # 跳过首行0

# 读取关联矩阵（自动跳过首行标题）
didr_df = pd.read_csv('./Cdataset_csv_output/didr.csv', header=None, skiprows=1)

# 转置矩阵（现在行是药物，列是疾病）
drug_disease_df = didr_df.T.reset_index(drop=True)

# 处理每个药物的关联疾病
results = []
for drug_idx, row in drug_disease_df.iterrows():
    drug_id = drug_ids[drug_idx]

    # 收集所有关联疾病
    associated_diseases = [
        disease_ids[col_idx]
        for col_idx, value in enumerate(row)
        if value == 1
    ]

    # 构建结果字典
    drug_data = {
        "DrugID": drug_id,
        "DiseaseCount": len(associated_diseases)
    }

    # 动态添加疾病列
    for i, disease_id in enumerate(associated_diseases, 1):
        drug_data[f"AssociatedDiseases{i}"] = disease_id

    results.append(drug_data)

# 转换为DataFrame
result_df = pd.DataFrame(results)

# 重新排序列（固定前两列，后续按数字排序）
cols = ["DrugID", "DiseaseCount"] + sorted(
    [col for col in result_df.columns if col.startswith("AssociatedDiseases")],
    key=lambda x: int(x.replace("AssociatedDiseases", ""))
)
result_df = result_df[cols]

print(result_df.head())
result_df.to_csv('./Cdataset_csv_output/drug_disease_ID.csv', index=False)
