import pandas as pd
from pathlib import Path

class Tools:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(self.file_path)

    def get_yearly_by_id(self, id, column_range=None):
        # 指定されたIDに対応する行を抽出
        extracted_rows = self.df[self.df['USER_ID'] == id]

        # USER_ID列を除外したデータフレームを作成
        extracted_rows_without_id = extracted_rows.drop(columns=['USER_ID'])

        # 列の範囲が指定されている場合、その範囲内の列に限定
        if column_range is not None:
            extracted_rows_without_id = extracted_rows_without_id.loc[:, column_range]

        # 抽出された行で値が1の列名を取得
        columns_with_value = extracted_rows_without_id.loc[:, (extracted_rows_without_id == 1).any()].columns.tolist()

        # 特定の列 "BDMQ4" を抽出
        yearly = extracted_rows[["BDMQ4"]]

        return yearly, columns_with_value


# 使用例
relative_path = Path(__file__).parent
file_path = relative_path / "data" / "raw_hobbyFix.csv"
t = Tools(file_path)

# DataFrame全体を読み込んで列範囲を取得
df = pd.read_csv(file_path)
column_range = df.columns[1:10]  # USER_ID列とBDMQ4列を除いた範囲を指定

# IDが2のユーザーのデータを取得、指定した列範囲を使用
print(t.get_yearly_by_id(1, column_range=column_range))
