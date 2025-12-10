import os
import requests

# 下载 FAERS ASCII 的脚本

# 设置保存目录
out_dir = "faers_data"
os.makedirs(out_dir, exist_ok=True)

# 定义要下载的年份和季度
years = list(range(2015, 2026))  # 例如 2015–2025 年
quarters = ["Q1", "Q2", "Q3", "Q4"]

base_url = "https://fis.fda.gov/content/Exports/faers_ascii_{year}{quarter}.zip"

for year in years:
    for q in quarters:
        url = base_url.format(year=year, quarter=q)
        filename = os.path.join(out_dir, f"faers_ascii_{year}{q}.zip")
        try:
            print(f"Downloading {url} ...")
            resp = requests.get(url, timeout=60)
            if resp.status_code == 200:
                with open(filename, "wb") as f:
                    f.write(resp.content)
                print(f"Saved to {filename}")
            else:
                print(f"  → Failed: status code {resp.status_code}")
        except Exception as e:
            print(f"  → Error: {e}")
