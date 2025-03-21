import scipy.io
import pandas as pd
import os
import numpy as np  # 添加缺失的numpy导入


def mat_to_csv(mat_file_path, output_folder):
    # 加载MAT文件
    mat_data = scipy.io.loadmat(mat_file_path)

    # 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)

    # 遍历所有变量
    for var_name in mat_data:
        # 跳过MATLAB系统变量
        if var_name.startswith('__'):
            continue

        data = mat_data[var_name]

        try:
            # 处理标准数组（现在已正确引用np）
            if isinstance(data, np.ndarray):
                df = pd.DataFrame(data)

                # 处理结构化数组
                if data.dtype.names:
                    df = pd.DataFrame(data.item(), columns=data.dtype.names)

                # 处理多维数组
                if len(data.shape) > 2:
                    print(f"变量 {var_name} 是多维数组（shape: {data.shape}），可能需要特殊处理")
                    continue

                # 保存为CSV
                csv_path = os.path.join(output_folder, f"{var_name}.csv")
                df.to_csv(csv_path, index=False)
                print(f"已保存：{csv_path}")

        except Exception as e:
            print(f"处理变量 {var_name} 时出错: {str(e)}")


# 使用示例
if __name__ == "__main__":
    mat_file = "Cdataset.mat"  # 替换为你的文件路径
    output_dir = "Cdataset_csv_output"  # 输出目录

    mat_to_csv(mat_file, output_dir)
    print("转换完成！")
