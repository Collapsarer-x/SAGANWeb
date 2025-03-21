import requests
import json

# 提供 API Key
API_KEY = "64d96db7-ae99-44ac-bd5a-2f41cbe4d775"
DISEASE_ID = "125851"  # 需要查询的疾病 ID
DISEASE_IDENT = "OMIM_"

DISEASE_ID = DISEASE_IDENT + DISEASE_ID

# API 请求 URL
url = f"https://api.disgenet.com/api/v1/dda?disease={DISEASE_ID}"

# HTTP 头部信息
headers = {
    "Authorization": API_KEY,
    "accept": "application/json"
}

# 发送请求
response = requests.get(url, headers=headers)

# 处理响应
if response.status_code == 200:
    data = response.json()

    # 保存整个 JSON 文件
    with open(f"{DISEASE_ID}_disease_disease.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    # 提取并排序疾病数据（按 Jaccard 指数排序）
    diseases = sorted(data["payload"], key=lambda x: x["jaccard_genes"], reverse=True)[:5]

    # 显示前 5 个疾病
    print("Top 5 Disease Associations:")
    for disease in diseases:
        print(f"Disease: {disease['disease2_Name']}, OMIM ID: {disease['disease2_Vocabularies'][0]}, Jaccard Index: {disease['jaccard_genes']:.2f}")
else:
    print(f"Error: {response.status_code}, {response.text}")
