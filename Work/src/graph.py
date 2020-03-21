# -----------------------------------
# DBから始点と終点を取得し，グラフを描画
# -----------------------------------

from graphviz import Digraph
import sqlite3

# DBの名前
dbname = "../DB/nodes.db"

# DB接続
conn = sqlite3.connect(dbname)
c = conn.cursor()

# select文を実行
# 始点と終点を取得
c.execute("select start, end from nodes;")

# 始点となる回数（辞書型）
counter = {}

"""
# select で取ってきた各行に対して実行
for row in c:
    # 辞書内にキーが存在しなければ，値を0にする
    counter.setdefault(str(row[0]), 0)
    # 始点の回数を+1
    counter[str(row[0])] += 1
"""

# 有向グラフ
graph = Digraph(format="png")

# select で取ってきた各行に対して実行
for row in c:
    # グラフ作成
    graph.edge(str(row[0]), str(row[1]))

# DB閉じる
conn.commit()
conn.close()


# 画像表示
graph.view()
