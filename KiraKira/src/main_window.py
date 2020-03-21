# ---------------
# メインウィンドウ
# ---------------

import wx
import sqlite3


class mainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "メイン", size=(1600, 900), pos=(0, 0))

        # ----- パネルの設定 -----
        show_panel = wx.Panel(self, -1, pos=(0, 0), size=(1000, 900))
        show_panel.SetBackgroundColour("cyan")

        input_panel = wx.Panel(self, -1, pos=(1000, 0), size=(600, 900))
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

        # 部品の設定
        # no_imageの画像
        image = wx.Image("../image/no_image_small.png")
        bitmap = image.ConvertToBitmap()
        # 次へボタン
        button_next = wx.Button(input_panel, -1, "次へ", pos=(450, 10), size=(120, 40))
        button_next.SetFont(font)
        # やることラベル
        label_todo = wx.StaticText(input_panel, -1, "やること", pos=(100, 100))
        label_todo.SetFont(font)
        # やることテキストボックス
        textbox_todo = wx.TextCtrl(input_panel, -1, pos=(100, 150), size=(400, 40))
        textbox_todo.SetFont(font)
        # やるひとラベル
        label_todo = wx.StaticText(input_panel, -1, "やるひと", pos=(100, 250))
        label_todo.SetFont(font)
        # 登録するボタン
        button_register = wx.Button(input_panel, -1, "登録する", pos=(200, 750), size=(200, 50))
        button_register.SetFont(font)
        # 画像1
        image1 = wx.StaticBitmap(input_panel, -1, bitmap=bitmap, pos=(100, 300))
        # チェックボックス1
        checkbox1 = wx.CheckBox(input_panel, -1, pos=(150, 450), size=(30, 30))
        # 画像2
        image1 = wx.StaticBitmap(input_panel, -1, bitmap=bitmap, pos=(230, 300))
        # チェックボックス2
        checkbox1 = wx.CheckBox(input_panel, -1, pos=(280, 450), size=(30, 30))
        # 画像3
        image1 = wx.StaticBitmap(input_panel, -1, bitmap=bitmap, pos=(360, 300))
        # チェックボックス3
        checkbox1 = wx.CheckBox(input_panel, -1, pos=(410, 450), size=(30, 30))
        # 画像4
        image1 = wx.StaticBitmap(input_panel, -1, bitmap=bitmap, pos=(165, 500))
        # チェックボックス4
        checkbox1 = wx.CheckBox(input_panel, -1, pos=(215, 650), size=(30, 30))
        # 画像5
        image1 = wx.StaticBitmap(input_panel, -1, bitmap=bitmap, pos=(295, 500))
        # チェックボックス5
        checkbox1 = wx.CheckBox(input_panel, -1, pos=(345, 650), size=(30, 30))

        # ----- input_panel ここまで -----


if __name__ == "__main__":
    app = wx.App()
    frame = mainFrame()
    frame.Show()
    app.MainLoop()
