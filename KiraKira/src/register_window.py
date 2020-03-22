# -------------
# 登録ウィンドウ
# -------------

import wx
from split import Split

class registerFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "登録ウィンドウ", size=(1600, 900), pos=(0, 0))

        # ListCtrl の行数
        self.listctrl_rows = 0

        # ----- パネルの設定 -----
        console_panel = wx.Panel(self, -1, pos=(30, 30), size=(940, 810))
        console_panel.SetBackgroundColour("cyan")

        info_panel = wx.Panel(self, -1, pos=(1000, 0), size=(600, 900))
        info_panel.SetBackgroundColour("green")


        # ----- console_panel ここから -----

        # 表形式で表示
        style = wx.LC_REPORT | wx.LC_HRULES | wx.LC_NO_HEADER
        self.listctrl = wx.ListCtrl(console_panel, -1, pos=(0, 0),size=(940, 770),  style=style)
        font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.listctrl.SetFont(font)

        # カラム
        self.listctrl.InsertColumn(0, "log", wx.LIST_FORMAT_LEFT, 600)

        # テキストボックス
        self.textbox_console = wx.TextCtrl(console_panel, -1, pos=(0, 770), size=(940, 40))
        self.textbox_console.SetFont(font)
        self.textbox_console.Bind(wx.EVT_KEY_DOWN, self.onKeyDown) # キー押下と関数を関連付ける

        # ----- console_panel ここまで -----


        # ----- info_panel ここから -----

        # 部品の設定
        # 前へボタン
        button_prev = wx.Button(info_panel, -1, "前へ", pos=(320, 10), size=(120, 40))
        button_prev.SetFont(font)
        button_prev.Bind(wx.EVT_BUTTON, self.onPrevButtonClick) # ボタンを関数を関連付ける
        # 次へボタン
        button_next = wx.Button(info_panel, -1, "次へ", pos=(450, 10), size=(120, 40))
        button_next.SetFont(font)
        button_next.Bind(wx.EVT_BUTTON, self.onNextButtonClick) # ボタンを関数を関連付ける

        # ----- info_panel ここまで -----
    

    # テキストボックス中でキーが押されると呼び出される．
    # Enterキーに反応しない・・・ 仕方がないのでescapeキーで代用
    def onKeyDown(self, event):
        key = event.GetKeyCode()
        #if key == wx.WXK_RETURN:
            #print("ENTERキー押したね？")
            #self.writeListCtrl()
        
        if key == wx.WXK_ESCAPE:
            self.writeListCtrl()
        
        else:
            event.Skip()
    

    # ListCtrl に書き込み
    def writeListCtrl(self):
        # テキストボックスからの入力
        str_input = self.textbox_console.GetValue()

        # Split のインスタンス化
        spl = Split()
        # 構文チェック済みの文字列
        syntax_checked = spl.syntax_check(str_input)

        if syntax_checked == None:
            print("チェック通らず")
            # 行追加
            self.listctrl.InsertItem(self.listctrl_rows, "構文エラーです")
        else:
            # 行追加
            self.listctrl.InsertItem(self.listctrl_rows, syntax_checked)
        
        # 行数 +1
        self.listctrl_rows += 1
        # テキストボックス初期化
        self.textbox_console.SetValue("")
    

    # 次へボタンクリック時に呼び出される
    def onNextButtonClick(self, event):
        # ウィンドウを閉じる
        self.Destroy()

        print("グラフ表示準備中...")
        # graph_window.py を実行
        import graph_window
    

    # 前へボタンクリック時に呼び出される
    def onPrevButtonClick(self, event):
        # ウィンドウを閉じる
        self.Destroy()

        # main_window.py を実行
        from main_window import mainFrame
        app = wx.App()
        frame = mainFrame()
        frame.Show()
        app.MainLoop()



if __name__ == "__main__":
    app = wx.App()
    frame = registerFrame()
    frame.Show()
    app.MainLoop()