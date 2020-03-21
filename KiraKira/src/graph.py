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
# メンバー名を取得
c.execute("select distinct member1 from todo_and_member;")

# メンバー名を格納するリスト
members = []

# select文で取得した各行に対して実行
# 全ユーザ名を取得
for row in c:
    # ユーザ名が無ければスキップ
    if str(row[0]) == "":
        continue

    # メンバーのリストに追加
    members.append(str(row[0]))

# ノードに付ける色
colors = ["pink", "cyan", "greenyellow", "yellow", "orange"]

# メンバー名と色を対応付ける辞書
member_and_color = {}

# メンバー名と色を対応付ける
for i in range(len(members)):
    member_and_color[members[i]] = colors[i]


# select文を実行
# 始点，終点，メンバー名（二人分）を取得
c.execute("select start, end, member1, member2 from nodes, todo_and_member where start=TODO_ID order by start;")

# select文で取得した各行に対して実行
for row in c:
    # メンバーが複数いる場合（カラムmember2が空文字列でない場合）は色を変えない
    if str(row[3]) != "":
        graph.attr("node", color="black")
        continue
    
    # メンバーが決まっている場合（カラムmember1が空文字列でない場合）は色を付ける
    if str(row[2]) != "":
        # 始点を強調する
        graph.attr("node", color="red")
        graph.node(str(row[0]), color="black", style="filled", fillcolor=member_and_color[str(row[2])], fontcolor="black")
        # 終点はそのまま
        graph.attr("node", color="black")
        graph.node(str(row[1]))

    # 辺の作成
    graph.edge(str(row[0]), str(row[1]))


# 始点となる回数を数えて，回数の多いものに色を付ける
"""
# select文を実行
# 始点を取得
c.execute("select start from nodes;")

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


# 特定のノードに色付けする時（確認用）
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


# 画像を保存
graph.render("../image/graph")

# 画像表示
graph.view()
