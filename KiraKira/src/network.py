#=======================================
# DBから始点と終点を取得し，グラフを描画
#=======================================
import matplotlib.pyplot as plt
import networkx as nx
import sqlite3

# DBの名前
dbname = "DB/nodes.db"

# 有向グラフ
Graph = nx.DiGraph()

# 頂点の一覧(set型)
nodes = set()

# DB接続
conn = sqlite3.connect(dbname)
c = conn.cursor()

# select文を実行
# 始点と終点を取得
c.execute("select start, end from nodes;")

# select で取ってきた各行に対して実行
for row in c:
    # 点の一覧に追加
    nodes.add(str(row[0]))
    nodes.add(str(row[1]))
    Graph.add_nodes_from(list(nodes))

    # 辺追加
    Graph.add_edge(str(row[0]), str(row[1]))

    # 出力
    #print(str(row[0]) + ", " + str(row[1]))

# DB閉じる
conn.commit()
conn.close()


# レイアウトの取得
pos = nx.spring_layout(Graph)

# 可視化
plt.figure(figsize = (6,6))
nx.draw_networkx(Graph,pos)
#nx.draw_networkx_nodes(Graph,pos)
plt.axis('off')
plt.show()