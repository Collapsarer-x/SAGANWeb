import csv

# 读取CSV文件
with open('./Cdataset_csv_output/Wdname.csv', 'r') as file:
    reader = csv.reader(file)
    # 提取每行的数字部分
    data = [row[0].replace("D", "").replace("'", "").replace("[", "").replace("]", "") for row in reader]

# 写入新的CSV文件
with open('疾病/Cdataset_Wd.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for item in data:
        writer.writerow([item])

print("处理完成，结果已保存到 Fdataset_Wd.csv")