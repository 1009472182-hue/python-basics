import os
import zipfile

# ====== 配置你的 FAERS ZIP 文件所在目录 ======
base_dir = r"E:\学习资料\硕士\广医二院相关资料\PD-1免疫抑制剂治疗肝癌的临床综合评价\FAERS数据库"

# ====== 扫描目录中的所有 ZIP 文件 ======
for filename in os.listdir(base_dir):
    if filename.lower().endswith(".zip"):
        zip_path = os.path.join(base_dir, filename)

        # 去掉 ".zip" 后的文件夹名，例如 faers_ascii_2017Q1
        folder_name = filename[:-4]
        extract_dir = os.path.join(base_dir, folder_name)

        # 如果文件夹不存在则创建
        if not os.path.exists(extract_dir):
            os.makedirs(extract_dir)

        print(f"解压中：{zip_path} → {extract_dir}")

        # ====== 解压 ZIP 文件 ======
        try:
            with zipfile.ZipFile(zip_path, 'r') as zf:
                zf.extractall(extract_dir)
            print("  ✓ 解压完成")
        except Exception as e:
            print(f"  ✗ 解压失败：{e}")

print("\n全部 ZIP 文件处理完毕！")
