import csv

# 读取第一个文件 Cdataset_Wd.csv
with open('Cdataset_Wd.csv', 'r') as file1:
    reader1 = csv.reader(file1)
    data1 = set(row[0] for row in reader1 if row[0] != '0')  # 忽略第一行的 '0'

# 读取第二个文件 Fdataset_Wd.csv
with open('Fdataset_Wd.csv', 'r') as file2:
    reader2 = csv.reader(file2)
    data2 = set(row[0] for row in reader2 if row[0] != '0')  # 忽略第一行的 '0'

# 合并两个数据集并去重
merged_data = data1.union(data2)

# 将结果写入新的CSV文件
with open('../../DiseaseDatasets/Disease/Merged_OMIMID.csv', 'w', newline='') as merged_file:
    writer = csv.writer(merged_file)
    writer.writerow(['0'])  # 写入第一行的 '0'
    for number in sorted(merged_data, key=int):  # 按数字大小排序
        writer.writerow([number])

print("合并完成，结果已保存到 Merged_OMIMID.csv")