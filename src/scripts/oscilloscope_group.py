import os
import pandas as pd
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science','ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'

def get_csv_filenames(directory):
    # 指定ディレクトリからCSVファイル名のリストを取得
    return [f for f in os.listdir(directory) if f.endswith('.csv')]

def plot_grouped_by(directory, group_by='p'):
    filenames = get_csv_filenames(directory)
    data_groups = {}

    # ファイル名からpとdの値を抽出し、辞書に格納する
    for filename in filenames:
        parts = filename.split('-')
        p_value = parts[0][1:]  # 'p'の後の数値を抽出
        d_value = parts[1][1:]  # 'd'の後の数値を抽出
        key = p_value if group_by == 'p' else d_value

        # グループをキーにしてファイル名を追加
        if key not in data_groups:
            data_groups[key] = []
        data_groups[key].append(filename)

    # 各グループに対してプロットする
    for key, files in data_groups.items():
        plt.figure(figsize=(8, 6))
        for filename in files:
            label = filename.split('-oscilloscope')[0]
            filepath = os.path.join(directory, filename)
            data = pd.read_csv(filepath)
            data['x'] = data['x'] - data['x'].iloc[0]
            plt.plot(data['x'], data[' y'], label=label)

        plt.xlabel('Time $t$ / s')
        plt.ylabel('Voltage $V$ / V')
        plt.legend()
        plt.savefig(f"../figures/oscilloscope-grouped/{group_by}-{key}.png")
        plt.close()

# 実際のディレクトリパスを指定
directory = '../data/oscilloscope'

plot_grouped_by(directory, group_by='p')

plot_grouped_by(directory, group_by='d')
