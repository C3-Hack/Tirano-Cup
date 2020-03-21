# -----------------------------------
# DBから始点と終点を取得し，グラフを描画
# -----------------------------------

from graphviz import Digraph
import sqlite3

# 有向グラフ
graph = Digraph(format="png")

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

# select で取ってきた各行に対して実行
# まずは各ノードが始点となる回数を調べる
for row in c:
    # 辞書内にキーが存在しなければ，値を0にする
    counter.setdefault(str(row[0]), 0)
    # 始点の回数を+1
    counter[str(row[0])] += 1

# counterのvaluesを集めて昇順に並び変え
cnt_num = sorted(set(counter.values()))

# select文をもう一回実行
# 始点と終点を取得
c.execute("select start, end from nodes;")

# select で取ってきた各行に対して実行
for row in c:
    # 始点となる回数が最大のノードに色付け
    if counter[row[0]] == cnt_num[-1]:
        # 始点を強調する
        graph.attr("node", color="red")
        graph.node(str(row[0]), color="black", style="filled", fillcolor="red", fontcolor="black")
        # 終点はそのまま
        graph.attr("node", color="black")
        graph.node(str(row[1]))
    
    # 始点となる回数が2番目に大きいノードに色付け
    elif counter[row[0]] == cnt_num[-2]:
        # 始点を強調する
        graph.attr("node", color="darkorange")
        graph.node(str(row[0]), color="black", style="filled", fillcolor="darkorange", fontcolor="black")
        # 終点はそのまま
        graph.attr("node", color="black")
        graph.node(str(row[1]))
    
    # その他
    else:
        # そのままにする
        graph.attr("node", color="black")

    # 辺の作成
    graph.edge(str(row[0]), str(row[1]))

"""
# 色づけしたいノード
with_color = ["A", "B", "I", "O", "R", "S"]

for row in c:
    if str(row[0]) in with_color:
    # 始点を強調する
        graph.attr("node", color="red")
        graph.node(str(row[0]), style="filled", fillcolor="red", fontcolor="black")
        # 終点はそのまま
        graph.attr("node", shape="circle", color="black")
        graph.node(str(row[1]))
    else:
        # そのままにする
        graph.attr("node", shape="circle", color="black")
    
    graph.edge(str(row[0]), str(row[1]))
"""

# DB閉じる
conn.commit()
conn.close()


# 画像表示
graph.view()
