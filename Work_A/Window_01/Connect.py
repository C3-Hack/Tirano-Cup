import wx
import sqlite3

####登録画面のクラス
class Connect(wx.Frame):
    def __init__(self,parent,id):
        ##フレーム
        wx.Frame.__init__(self,parent,id,"コネクション",size=(1400,800))

        font = wx.Font(30, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        ##パネル
        splitter = wx.SplitterWindow(self, wx.ID_ANY, style=wx.SP_LIVE_UPDATE)
        splitter.SetMinimumPaneSize(100)
        ##左側のパネル
        self.left_panel = wx.Panel(splitter, wx.ID_ANY, style=wx.BORDER_SUNKEN)
        self.left_panel.SetBackgroundColour(wx.WHITE)
        ##右側のパネル
        self.right_panel = wx.Panel(splitter, wx.ID_ANY, style=wx.BORDER_SUNKEN)
        self.right_panel.SetBackgroundColour(wx.RED)

        splitter.SplitVertically(self.left_panel, self.right_panel)
        ##テキスト
        self.v_layout = wx.BoxSizer(wx.VERTICAL)
        ##左側でのテキスト
        self.todo_l=wx.StaticText(self.left_panel,-1, "コマンドのログ",pos=(350,10))
        self.todo_l.SetFont(font)
        ##右側

        ##やること入力フォーム
        self.todo_enter= wx.TextCtrl(self.right_panel, -1,pos=(50,700),size=(500,40))
        self.todo_enter.SetFont(font)

        ##登録ボタン

        self.button_r = wx.Button(self.right_panel,-1, '実行する',pos=(550,710))
        ##登録ボタンを押すとlog関数の処理に移る
        self.Bind(wx.EVT_BUTTON,self.log,self.button_r)

        self.left_panel.SetSizer(self.v_layout)
        ##フレームを公開する
        self.Show()

    def log(self,event):
        #入力した文字列を使えるようにした
        self.enter_w=self.todo_enter.GetValue()
        text = wx.StaticText(self.left_panel, wx.ID_ANY,self.enter_w )
        #きれいに列挙する
        self.v_layout.Add(text, proportion=0)
        self.v_layout.Layout()



####実装
if __name__ == '__main__':
    app = wx.PySimpleApp()
    Connect(parent=None,id=-1)
    app.MainLoop()
