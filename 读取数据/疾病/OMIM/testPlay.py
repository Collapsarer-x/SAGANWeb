def omim_to_efo(omim_id):
    """OMIM转EFO ID（2025年验证版本）"""
    query = """
    query OmimToEfo($curie: String!) {
      disease(fromCurie: $curie) {
        id
        crossReferences {
          source
          reference
        }
      }
    }
    """

    variables = {"curie": f"Disease:{omim_id}"}

    try:
        response = requests.post(
            "https://platform.opentargets.org/api/graphql",
            headers={
                "Content-Type": "application/json",
                "OT-Client": "Disease-Converter/1.0"
            },
            json={"query": query, "variables": variables},
            timeout=10
        )

        if response.status_code != 200:
            print(f"HTTP错误 {response.status_code}")
            print("响应头:", response.headers)
            return None

        data = response.json()
        print("原始响应:", json.dumps(data, indent=2))  # 调试输出

        if 'errors' in data:
            print(f"GraphQL错误：{data['errors'][0]['message']}")
            return None

        if not data['data']['disease']:
            print(f"未找到OMIM:{omim_id}对应的疾病")
            return None

        # 精确匹配EFO ID
        efo_id = data['data']['disease']['id']
        if efo_id.startswith("EFO_"):
            return efo_id

        # 从交叉引用中查找
        for xref in data['data']['disease']['crossReferences']:
            if xref['source'] == 'EFO':
                return xref['reference']

        return None

    except Exception as e:
        print(f"请求异常: {str(e)}")
        return None
