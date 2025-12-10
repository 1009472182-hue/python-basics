import os
import requests

# 下载 FAERS ASCII 的脚本

# 设置保存目录
out_dir = r"E:\学习资料\硕士\广医二院相关资料\PD-1免疫抑制剂治疗肝癌的临床综合评价\FAERS数据库"
os.makedirs(out_dir, exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Connection": "keep-alive",
}

# 定义要下载的年份和季度
years = list(range(2020, 2021))  # 例如 2014–2020 年
quarters = ["Q1", "Q2", "Q3", "Q4"]

base_url = "https://fis.fda.gov/content/Exports/faers_ascii_{year}{quarter}.zip"

for year in years:
    for q in quarters:
        url = base_url.format(year=year, quarter=q)
        filename = os.path.join(out_dir, f"faers_ascii_{year}{q}.zip")
        try:
            print(f"Downloading {url} ...")
            resp = requests.get(url, headers=headers, timeout=60, stream=True)
            if resp.status_code == 200:
                with open(filename, "wb") as f:
                    f.write(resp.content)
                print(f"Saved to {filename}")
            else:
                print(f"  → Failed: status code {resp.status_code}")
        except Exception as e:
            print(f"  → Error: {e}")
