import os
import pandas as pd
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science','ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'

def plot_csv_files(directory):
    # 指定されたディレクトリ内のすべてのCSVファイルを探索
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            # CSVファイルを読み込む
            filepath = os.path.join(directory, filename)
            data = pd.read_csv(filepath)

            # グラフをプロット
            plt.figure()
            plt.plot(data['x'], data[' y'])
            plt.xlabel('Time $t$ / s')
            plt.ylabel('Voltage $V$ / V')

            # グラフを画像として保存
            plt.savefig("../figures/oscilloscope-each/" + filename + ".png")
            plt.close()  # メモリ解放

# ディレクトリパスを指定して関数を呼び出す
plot_csv_files('../data/oscilloscope')
