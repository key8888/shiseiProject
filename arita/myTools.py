import pandas as pd
from pathlib import Path


class Tools:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(self.file_path)
        # self.adjective_mapping = {".1": "個性的", ".2": "存在感がある", ".3": "品のある", ".4": "洗練された",
        #                           ".5": "身近なもの", ".6": "飽きない", ".7": "伝統的", ".8": "モダンな",
        #                           ".9": "親しみやすい", ".10": "可愛らしい", ".11": "日常的に使う",
        #                           ".12": "特別な日に使う", ".13": "贈り物に適する", ".14": "最も好き",
        #                           ".15": "普通に好き", ".16": "好みでない"}
        # self.name_mapping = {"Q1": [], "Q2": [], "Q3": [], "Q4": []}

    def get_yearly_by_id(self, id, column_range_begin, column_range_end):
        # 指定されたIDに対応する行を抽出
        extracted_rows = self.df[self.df['USER_ID'] == id]

        # USER_ID列を除外したデータフレームを作成
        extracted_rows_without_id = extracted_rows.drop(columns=['USER_ID'])

        # 列の範囲が指定されている場合、その範囲内の列に限定
        if column_range_begin is not None and column_range_end is not None:
            extracted_rows_without_id = extracted_rows_without_id.loc[:,
                                        self.df.columns[column_range_begin:column_range_end]]

        # 抽出された行で値が1の列名を取得
        columns_with_value = extracted_rows_without_id.loc[:, (extracted_rows_without_id == 1).any()].columns.tolist()

        # 特定の列 "BDMQ4" を抽出
        yearly = extracted_rows[["BDMQ4"]]

        return yearly, columns_with_value




# 使用例
relative_path = Path(__file__).parent
file_path = relative_path / "data" / "raw_hobbyFix.csv"
t = Tools(file_path)

# # DataFrame全体を読み込んで列範囲を取得
# df = pd.read_csv(file_path)
# column_range = df.columns[1:10]  # USER_ID列とBDMQ4列を除いた範囲を指定

# IDが2のユーザーのデータを取得、指定した列範囲を使用
print(t.get_yearly_by_id(1, 1, 562))
