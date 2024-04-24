import os
import pandas as pd
import matplotlib.pyplot as plt
import re
import scienceplots

plt.style.use(['science','ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'

def sort_filenames(filenames):
    # ファイル名からpとdの値を抽出し、これに基づいてソートする
    def extract_sort_values(filename):
        parts = filename.split('-')
        p_value = int(parts[0][1:])  # 'p'の後の数値を抽出
        d_value = int(parts[1][1:])  # 'd'の後の数値を抽出
        return (p_value, d_value)  # dでソート後、pでソート

    # ソート処理
    filenames.sort(key=extract_sort_values)

def plot_all_csvs_in_one(directory):
    plt.figure(figsize=(8, 6))

    # 指定されたディレクトリ内のすべてのCSVファイルを探索
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    sort_filenames(csv_files)

    # ソートされたファイル名でループ
    for filename in csv_files:
        if filename.endswith('.csv'):
            label = filename.split('-oscilloscope')[0]

            filepath = os.path.join(directory, filename)
            data = pd.read_csv(filepath)

            data['x'] = data['x'] - data['x'].iloc[0]

            plt.plot(data['x'], data[' y'], label=label)

    # グラフのタイトルと軸ラベルを設定
    plt.xlabel('Time $t$ / s')
    plt.ylabel('Voltage $V$ / V')
    plt.legend()

    plt.savefig("../figures/oscilloscope/oscilloscope.png")
    plt.close()

plot_all_csvs_in_one('../data/oscilloscope')
