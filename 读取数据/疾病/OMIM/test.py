import os
import time
import random
import pandas as pd
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth
from bs4 import BeautifulSoup


# ==========================
# 1. 解析 mim2gene.txt 获取 MIM 列表
# ==========================
def read_mim2gene(file_path):
    mim_list = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.startswith("#"):  # 跳过注释
                fields = line.strip().split("\t")
                if len(fields) >= 2 and "moved" not in fields[1]:  # 排除已移除的 MIM
                    mim_number = fields[0]
                    mim_list.append(mim_number)
    return mim_list


from playwright.sync_api import sync_playwright


def bypass_playwright_detection(page):
    """ 规避 Playwright 被检测的方法 """

    page.evaluate("""
        () => {
            // 删除 navigator.webdriver
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });

            // 伪装语言
            Object.defineProperty(navigator, 'languages', {
                get: () => ['en-US', 'en']
            });

            // 伪装插件
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5]
            });

            // 伪装设备内存
            Object.defineProperty(navigator, 'deviceMemory', {
                get: () => 8
            });

            // 禁用 WebRTC 泄露 IP
            Object.defineProperty(navigator, 'hardwareConcurrency', {
                get: () => 4
            });
        }
    """)


# ==========================
# 2. 爬取 Disease 页面
# ==========================
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth
import os
import time
import random
from playwright.sync_api import sync_playwright


def bypass_playwright_detection(page):
    """ 规避 Playwright 被检测的方法 """
    page.evaluate("""
        () => {
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
            Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
            Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5] });
            Object.defineProperty(navigator, 'deviceMemory', { get: () => 8 });
            Object.defineProperty(navigator, 'hardwareConcurrency', { get: () => 4 });
        }
    """)


def fetch_omim_page(mim_number, save_dir="entry"):
    """ 爬取 Disease 页面并规避检测 """

    url = f"https://omim.org/entry/{mim_number}"
    os.makedirs(save_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        # 规避 Playwright 检测
        bypass_playwright_detection(page)

        try:
            print(f"正在爬取 {mim_number} ...")
            page.goto(url, timeout=30000)
            time.sleep(random.uniform(3, 6))  # 伪装真实用户

            with open(f"{save_dir}/{mim_number}.html", "w", encoding="utf-8") as f:
                f.write(page.content())

            print(f"成功爬取 {mim_number}")
        except Exception as e:
            print(f"爬取 {mim_number} 失败: {e}")
        finally:
            browser.close()


# 批量爬取
def run_spider(mim_list, max_pages=5):
    for index, mim_number in enumerate(mim_list[:max_pages]):  # 仅爬取 max_pages 个数据（可修改）
        fetch_omim_page(mim_number)
        time.sleep(random.uniform(5, 10))  # 5~10秒随机等待，防止过快请求


# ==========================
# 3. 解析 HTML 文件
# ==========================
def parse_omim_html(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "lxml")

    mim_number = os.path.basename(html_file).replace(".html", "")
    url = f"https://omim.org/entry/{mim_number}"

    # 获取标题
    try:
        title = soup.title.string.strip().split(mim_number + " - ")[1]
    except:
        title = "."

    # 获取表格信息
    table_info = []
    table = soup.find("table")
    if table:
        rows = table.find_all("tr")
        for row in rows:
            cols = [col.get_text(strip=True) for col in row.find_all("td")]
            if len(cols) >= 4:
                phenotype, mim_num, inheritance, mapping_key = cols[:4]
                table_info.append(f"{phenotype}|{mim_num}|{inheritance}|{mapping_key}")
    table_text = "; ".join(table_info) if table_info else "."

    # 获取临床描述
    clinical_desc = "."
    clinical_section = soup.select_one("#clinicalSynopsisFold")
    if clinical_section:
        clinical_desc = clinical_section.get_text(strip=True)

    # 获取详细描述
    description = "."
    desc_section = soup.select_one("#descriptionFold")
    if desc_section:
        description = desc_section.get_text(strip=True).replace("\n", " \\ ")

    return {
        "MimNum": mim_number,
        "Title": title,
        "Table": table_text,
        "Description": description,
        "Clinical": clinical_desc,
        "URL": url
    }


# 解析所有已爬取的 HTML
def parse_all_html(input_dir="entry", output_file="output.csv"):
    data = []
    for file in os.listdir(input_dir):
        if file.endswith(".html"):
            file_path = os.path.join(input_dir, file)
            parsed_data = parse_omim_html(file_path)
            data.append(parsed_data)

    # 转为 DataFrame 并保存
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False, encoding="utf-8")
    print(f"解析完成，结果保存至 {output_file}")


# ==========================
# 运行完整流程
# ==========================
mim2gene_file = "mim2gene.txt"  # 用户上传的文件路径
mim_list = read_mim2gene(mim2gene_file)

# 爬取前5个 MIM 页面（可修改 max_pages）
run_spider(mim_list, max_pages=5)

# 解析已爬取的 HTML 并保存结果
parse_all_html()
