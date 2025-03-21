import pandas as pd


def parse_id_file(content):
    return [line.strip("[]'\n ") for line in content.split('\n') if line.strip()]


# 读取映射文件
with open('./Cdataset_csv_output/Wdname.csv', 'r') as f:
    disease_ids = parse_id_file(f.read())[1:]  # 跳过首行0

with open('./Cdataset_csv_output/Wrname.csv', 'r') as f:
    drug_ids = parse_id_file(f.read())[1:]  # 跳过首行0

# 读取关联矩阵（自动跳过首行标题）
drug_df = pd.read_csv('./Cdataset_csv_output/drug.csv', header=None, skiprows=1)
disease_df = pd.read_csv('./Cdataset_csv_output/disease.csv', header=None, skiprows=1)


def process_dataframe(df, ids):
    """将ID列表同时设置为列名和行索引"""
    # 设置列名
    df.columns = ids
    # 设置行索引
    df.index = ids

    # 插入第一列
    df.insert(0, 'ID', ids)
    return df


# 对drug_df操作
drug_df1 = process_dataframe(drug_df, drug_ids)
drug_df1.to_csv('./Cdataset_csv_output/drug_ID.csv', index=False)

# 对disease_df操作
disease_df = process_dataframe(disease_df, disease_ids)
disease_df.to_csv('./Cdataset_csv_output/disease_ID.csv', index=False)
