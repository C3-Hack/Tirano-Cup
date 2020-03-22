# 画面遷移の例
# https://qiita.com/flour/items/01a7d08b5460c1d6bfeb

import wx

class mainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, 'Testapp', size=(900,500), style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)

        self.CreateStatusBar()
        self.SetStatusText('Testapp')
        self.GetStatusBar().SetBackgroundColour(None)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)

        self.set_screen(Panel_1)


    def set_screen(self,panel):
        self.sizer.Clear(False)
        self.DestroyChildren()

        self.now_panel=panel(self)
        self.sizer.Add(self.now_panel,1,wx.EXPAND)
        self.sizer.Layout()



class Panel_1(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, wx.ID_ANY)
        self.parent=parent

        title_text = wx.StaticText(self, wx.ID_ANY, 'タイトル', style=wx.TE_CENTER)
        font_Title = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        title_text.SetFont(font_Title)

        start_button = wx.Button(self, wx.ID_ANY, 'スタート')
        start_button.Bind(wx.EVT_BUTTON, self.click_start_button)

        layout = wx.BoxSizer(wx.VERTICAL)

        layout.Add(title_text, flag=wx.ALIGN_CENTER)
        layout.Add(start_button, flag=wx.ALIGN_CENTER)

        self.SetSizer(layout)

    def click_start_button(self, event):
        self.parent.set_screen(Panel_2)


class Panel_2(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, wx.ID_ANY)
        self.parent=parent

        title_text = wx.StaticText(self, wx.ID_ANY, '遷移後画面', style=wx.TE_CENTER)
        font_Title = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        title_text.SetFont(font_Title)

        start_button = wx.Button(self, wx.ID_ANY, 'スタートに戻る')
        start_button.Bind(wx.EVT_BUTTON, self.click_start_button)

        layout = wx.BoxSizer(wx.VERTICAL)

        layout.Add(title_text, flag=wx.ALIGN_CENTER)
        layout.Add(start_button, flag=wx.ALIGN_CENTER)

        self.SetSizer(layout)

    def click_start_button(self, event):
        self.parent.set_screen(Panel_1)

if __name__ == '__main__':

    application = wx.App()
    frame = mainFrame()
    frame.Show()
    application.MainLoop()