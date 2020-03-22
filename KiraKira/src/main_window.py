# ---------------
# メインウィンドウ
# ---------------

import wx
import sqlite3

# ----- DB 初期化 ----
# 接続
conn = sqlite3.connect("../DB/nodes.db")
c = conn.cursor()
# delete 文実行
c.execute("delete from nodes;")
c.execute("delete from todo_and_member;")
# 閉じる
conn.commit()
conn.close()

class mainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "メイン", size=(1600, 900), pos=(0, 0))

        # 登録時に使う
        self.id_counter = 0

        # ----- パネルの設定 -----
        show_panel = wx.Panel(self, -1, pos=(0, 0), size=(1000, 900))
        show_panel.SetBackgroundColour("cyan")

        input_panel = wx.Panel(self, -1, pos=(1000, 0), size=(600, 900))
        input_panel.SetBackgroundColour([200,255,200])


        # ----- show_panel ここから-----

        # 表形式で表示
        style = wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES
        self.listctrl = wx.ListCtrl(show_panel, -1, pos=(0, 0),size=(1000, 900),  style=style)
        font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.listctrl.SetFont(font)

        # カラム
        self.listctrl.InsertColumn(0, "やること", wx.LIST_FORMAT_LEFT, 600)
        self.listctrl.InsertColumn(1, "やるひと", wx.LIST_FORMAT_LEFT, 300)
        self.listctrl.InsertColumn(2, "ID", wx.LIST_FORMAT_LEFT, 100)

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
            self.listctrl.InsertItem(i, str(row[0]))
            self.listctrl.SetItem(i, 1, str(row[1]))
            self.listctrl.SetItem(i, 2, str(row[2]))
            i += 1

        # DB閉じる
        conn.commit()
        conn.close()

        # レイアウト設定
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(self.listctrl)
        show_panel.SetSizer(layout)

        # ----- show_panel ここまで -----

        # ----- input_panel ここから -----

        # 部品の設定
        # A-E の画像
        imageA = wx.Image("../image/A.png")
        bitmapA = imageA.ConvertToBitmap()
        imageB = wx.Image("../image/B.png")
        bitmapB = imageB.ConvertToBitmap()
        imageC = wx.Image("../image/C.png")
        bitmapC = imageC.ConvertToBitmap()
        imageD = wx.Image("../image/D.png")
        bitmapD = imageD.ConvertToBitmap()
        imageE = wx.Image("../image/E.png")
        bitmapE = imageE.ConvertToBitmap()
        # 次へボタン
        button_next = wx.Button(input_panel, -1, "次へ", pos=(450, 10), size=(120, 40))
        button_next.SetFont(font)
        button_next.Bind(wx.EVT_BUTTON, self.onNextButtonClick) # ボタンを関数を関連付ける
        # やることラベル
        label_todo = wx.StaticText(input_panel, -1, "やること", pos=(100, 100))
        label_todo.SetFont(font)
        # やることテキストボックス
        self.textbox_todo = wx.TextCtrl(input_panel, -1, pos=(100, 150), size=(400, 40))
        self.textbox_todo.SetFont(font)
        # やるひとラベル
        label_todo = wx.StaticText(input_panel, -1, "やるひと", pos=(100, 250))
        label_todo.SetFont(font)
        # 登録するボタン
        button_register = wx.Button(input_panel, -1, "登録する", pos=(200, 750), size=(200, 50))
        button_register.SetFont(font)
        button_register.Bind(wx.EVT_BUTTON, self.onRegisterButtonClick) # ボタンを関数を関連付ける
        
        
        # チェックボックス1-5
        self.checkbox1 = wx.CheckBox(input_panel, -1, pos=(150, 450), size=(30, 30))
        self.checkbox2 = wx.CheckBox(input_panel, -1, pos=(280, 450), size=(30, 30))
        self.checkbox3 = wx.CheckBox(input_panel, -1, pos=(410, 450), size=(30, 30))
        self.checkbox4 = wx.CheckBox(input_panel, -1, pos=(215, 650), size=(30, 30))
        self.checkbox5 = wx.CheckBox(input_panel, -1, pos=(345, 650), size=(30, 30))


        # 画像1
        image1 = wx.StaticBitmap(input_panel, -1, bitmap=bitmapA, pos=(80, 300))
        # チェックボックス1
        #checkbox1 = wx.CheckBox(input_panel, -1, pos=(150, 450), size=(30, 30))
        # 画像2
        image2 = wx.StaticBitmap(input_panel, -1, bitmap=bitmapB, pos=(230, 300))
        # チェックボックス2
        #checkbox2 = wx.CheckBox(input_panel, -1, pos=(280, 450), size=(30, 30))
        # 画像3
        image3 = wx.StaticBitmap(input_panel, -1, bitmap=bitmapC, pos=(380, 300))
        # チェックボックス3
        #checkbox3 = wx.CheckBox(input_panel, -1, pos=(410, 450), size=(30, 30))
        # 画像4
        image4 = wx.StaticBitmap(input_panel, -1, bitmap=bitmapD, pos=(155, 500))
        # チェックボックス4
        #checkbox4 = wx.CheckBox(input_panel, -1, pos=(215, 650), size=(30, 30))
        # 画像5
        image5 = wx.StaticBitmap(input_panel, -1, bitmap=bitmapE, pos=(305, 500))
        # チェックボックス5
        #checkbox5 = wx.CheckBox(input_panel, -1, pos=(345, 650), size=(30, 30))

        

        # ----- input_panel ここまで -----

    
    # 次へボタンクリック時に呼び出される
    def onNextButtonClick(self, event):

        # ウィンドウを閉じる
        self.Destroy()

        # register_window.py を実行
        from register_window import registerFrame

        app = wx.App()
        frame = registerFrame()
        frame.Show()
        app.MainLoop()


    # 登録するボタンクリック時に呼び出される
    def onRegisterButtonClick(self, event):
        # テキストボックスの入力
        str_todo = self.textbox_todo.GetValue()
        # チェックボックスのチェック
        join = {"A" : self.checkbox1.GetValue(),"B" : self.checkbox2.GetValue(), "C" : self.checkbox3.GetValue(), "D" : self.checkbox4.GetValue(), "E" : self.checkbox5.GetValue()}
        # メンバー
        members = []
        for k, v in join.items():
            if v:
                members.append(k)

        # 要素を5つにする
        for i in range(5 - len(members)):
            members.append("")

        # TODOのID
        IDs = [chr(i) for i in range(65, 65+26)]


        # DB接続
        conn = sqlite3.connect("../DB/nodes.db")
        c = conn.cursor()
        # SQL実行
        c.execute("insert into todo_and_member values(?,?,?,?,?,?,?);", (IDs[self.id_counter], str(str_todo), members[0], members[1], members[2], members[3], members[4]))
        
        self.listctrl.InsertItem(self.id_counter, str(str_todo))
        self.listctrl.SetItem(self.id_counter, 1, str(members[0]))
        self.listctrl.SetItem(self.id_counter, 2, IDs[self.id_counter])

        self.id_counter += 1

        # DB閉じる
        conn.commit()
        conn.close()

        # 入力内容の初期化
        self.textbox_todo.SetValue("")
        self.checkbox1.SetValue(False)
        self.checkbox2.SetValue(False)
        self.checkbox3.SetValue(False)
        self.checkbox4.SetValue(False)
        self.checkbox5.SetValue(False)




if __name__ == "__main__":
    app = wx.App()
    frame = mainFrame()
    frame.Show()
    app.MainLoop()
