import pandas as pd

def read_faers_chunked(path, chunk_size=100000):
    """按块读取 FAERS 数据，避免内存爆掉"""
    
    chunks = []
    try:
        # python engine + 分块读取
        for chunk in pd.read_csv(
            path,
            sep="$",
            engine="python",
            encoding="latin-1",
            dtype=str,
            chunksize=chunk_size,
            on_bad_lines="skip"
        ):
            chunks.append(chunk)
        return pd.concat(chunks, ignore_index=True)

    except Exception as e:
        print("chunk 模式失败，错误：", e)
        return None

import os
import pandas as pd

base_dir = r"E:\学习资料\硕士\广医二院相关资料\PD-1免疫抑制剂治疗肝癌的临床综合评价\FAERS数据库"

all_drug = []
all_reac = []
all_demo = []

print("\n开始扫描 FAERS 数据...\n")

for root, dirs, files in os.walk(base_dir):
    for fname in files:

        if not fname.lower().endswith(".txt"):
            continue

        fpath = os.path.join(root, fname)
        fname_upper = fname.upper()

        if fname_upper.startswith("DRUG"):
            print("读取 DRUG（分块读取）:", fpath)
            df = read_faers_chunked(fpath)
            if df is not None:
                all_drug.append(df)

        elif fname_upper.startswith("REAC"):
            print("读取 REAC（分块读取）:", fpath)
            df = read_faers_chunked(fpath)
            if df is not None:
                all_reac.append(df)

        elif fname_upper.startswith("DEMO"):
            print("读取 DEMO（分块读取）:", fpath)
            df = read_faers_chunked(fpath)
            if df is not None:
                all_demo.append(df)

# 输出目录
output_dir = os.path.join(base_dir, "合并结果")
os.makedirs(output_dir, exist_ok=True)

def save_excel(df_list, name):
    if not df_list:
        print(f"⚠ 没有发现 {name} 文件")
        return
    df = pd.concat(df_list, ignore_index=True)
    out_path = os.path.join(output_dir, f"ALL_{name}.xlsx")
    df.to_excel(out_path, index=False)
    print(f"✓ 已导出：{out_path}")

print("\n开始合并 >>>\n")

save_excel(all_drug, "DRUG")
save_excel(all_reac, "REAC")
save_excel(all_demo, "DEMO")

print("\n🎉 完成！所有数据已经成功处理。")
