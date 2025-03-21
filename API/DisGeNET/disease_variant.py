import requests
import json

# 提供 API Key
API_KEY = "64d96db7-ae99-44ac-bd5a-2f41cbe4d775"
DISEASE_ID = "125851"
DISEASE_IDENT = "OMIM_"

DISEASE_ID = DISEASE_IDENT + DISEASE_ID

# API 请求 URL
url = f"https://api.disgenet.com/api/v1/vda/summary?disease={DISEASE_ID}"

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
    with open(f"{DISEASE_ID}_disease_variant.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    # 提取并排序变体数据（按 `score` 排序）
    variants = sorted(data["payload"], key=lambda x: x.get("score", 0), reverse=True)[:5]

    # 显示前 5 个变体
    print("Top 5 Variants:")
    for variant in variants[:5]:
        variant_name = (
                variant.get("threeletterID_keyword") or
                variant.get("oneletterID_keyword") or
                ["N/A"]
        )[0]
        print(f"Variant: {variant_name}, ID: {variant['variantStrID']}, Score: {variant['score']:.2f}")
else:
    print(f"Error: {response.status_code}, {response.text}")
