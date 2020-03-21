# ---------------
# メインウィンドウ
# ---------------

import wx
import sqlite3


app = wx.App(False)

# ウィンドウの設定
frame = wx.Frame(None, -1, "メイン", size=(1600, 900), pos=(0, 0))


# ----- パネルの設定 -----
show_panel = wx.Panel(frame, -1, pos=(0, 0), size=(1000, 900))
show_panel.SetBackgroundColour("cyan")

input_panel = wx.Panel(frame, -1, pos=(1000, 0), size=(600, 900))
input_panel.SetBackgroundColour("green")


# ----- show_panel ここから-----

# 表形式で表示
style = wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES
listctrl = wx.ListCtrl(show_panel, -1, pos=(0, 0),size=(1000, 900),  style=style)
font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
listctrl.SetFont(font)

# カラム
listctrl.InsertColumn(0, "やること", wx.LIST_FORMAT_LEFT, 600)
listctrl.InsertColumn(1, "やるひと", wx.LIST_FORMAT_LEFT, 300)
listctrl.InsertColumn(2, "ID", wx.LIST_FORMAT_LEFT, 100)

# DBの名前
dbname = "../DB/nodes.db"

# DB接続
conn = sqlite3.connect(dbname)
c = conn.cursor()

# select文を実行
# やること，メンバー名，やることのIDを取得
c.execute("select TODO, member1, TODO_ID from todo_and_member;")

# select文で取得した各行に対して実行
i = 0
for row in c:
    # 行の追加
    listctrl.InsertItem(i, str(row[0]))
    listctrl.SetItem(i, 1, str(row[1]))
    listctrl.SetItem(i, 2, str(row[2]))
    i += 1

# DB閉じる
conn.commit()
conn.close()

# レイアウト設定
layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(listctrl)
show_panel.SetSizer(layout)

# ----- show_panel ここまで -----

# ----- input_panel ここから -----


# ----- input_panel ここまで -----


# 表示
frame.Show()
app.MainLoop()
