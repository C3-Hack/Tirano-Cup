# ------------------------
# グラフを表示するウィンドウ
# ------------------------

import wx
from PIL import Image

from graph import Utilities


app = wx.App(False)

# ウィンドウの設定
frame = wx.Frame(None, -1, "出力グラフ", size=(1600, 900), pos=(0, 0))

# パネルの設定
panel = wx.Panel(frame)

# 画像を取得
image = wx.Image("../image/graph_resized.png")
# bitmap に変換
bitmap = image.ConvertToBitmap()


# メンバー名と色の辞書
member_and_color_dict = Utilities().getMemberAndColorDict()

# 表示するテキストを作成
text = ""
for k, v in member_and_color_dict.items():
    text += "{}さん：{}, ".format(k, v)
# 最後のコンマとスペースを消す
text = text.rstrip(", ")

# ラベル設定
member_and_color_text = wx.StaticText(panel, -1, text)

# ラベルのフォント設定
font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
member_and_color_text.SetFont(font)


# レイアウト設定
layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(wx.StaticBitmap(panel, -1, bitmap=bitmap)) # 画像を表示
layout.Add(member_and_color_text)

panel.SetSizer(layout)

# 可視化
frame.Show()
# これがないとすぐ閉じる
app.MainLoop()