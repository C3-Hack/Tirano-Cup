# ------------------------
# グラフを表示するウィンドウ
# ------------------------

import wx
from PIL import Image


app = wx.App(False)

# ウィンドウの設定
frame = wx.Frame(None, -1, "出力グラフ", size=(1600, 900), pos=(0, 0))

# パネルの設定
panel = wx.Panel(frame)

# 画像を取得
image = wx.Image("../image/graph_resized.png")
# bitmap に変換
bitmap = image.ConvertToBitmap()

# レイアウト設定
layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(wx.StaticBitmap(frame, -1, bitmap=bitmap)) # 画像を表示
panel.SetSizer(layout)

# 可視化
frame.Show()
# これがないとすぐ閉じる
app.MainLoop()