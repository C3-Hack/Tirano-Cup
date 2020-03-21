import wx
import sqlite3

####エラー画面のクラス
class Error(wx.Frame):
    def __init__(self,parent):
        ##フレーム
        wx.Frame.__init__(self,parent,-1,"エラー",pos=(100,100),size=(600,300))
        panel = wx.Panel(self)

        ##テキスト
        font = wx.Font(40, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.errortext = wx.StaticText(panel,-1, '登録されているかプロジェクトが存在しません！',pos=(50,100))
        self.errortext.SetFont(font)
        ##閉じるボタン
        self.exitBtn = wx.Button(panel,label="卵で閉じる",pos=(500,250))
        self.Bind(wx.EVT_BUTTON,self.exit,self.exitBtn)

    ##ボタン実装
    def exit(self,event):
        self.Close(True)

####メンバー登録の画面
class add_member(wx.Frame,):
    def __init__(self,parent):
        ##フレーム
        wx.Frame.__init__(self,parent,1,"メンバー追加",pos=(300,300),size=(600,300))
        panel = wx.Panel(self)

        ##テキスト
        font = wx.Font(40, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.tourokuCtext = wx.StaticText(panel,-1, 'メンバーを追加する',pos=(50,100))
        self.tourokuCtext.SetFont(font)

        ##入力フォーム
        self.m_enter= wx.TextCtrl(panel, -1,pos=(50,200),size=(300,60))
        self.m_enter.SetFont(font)
        ##閉じるボタン
        self.exitBtn = wx.Button(panel,label="消す",pos=(500,100))
        self.Bind(wx.EVT_BUTTON,self.exit,self.exitBtn)
        ##追加ボタン
        self.add1 = wx.Button(panel,label="追加",pos=(500,250))
        self.Bind(wx.EVT_BUTTON,self.add,self.add1)

    def exit(self,event):
        self.Close(True)

    def add(self,event):
        self.m_enter_v=self.m_enter.GetValue()
        flag=0
        c=0
        ##Project-allのDBと接続
        connect = sqlite3.connect('Project_all.db')
        Project= connect.cursor()
        ##テーブルの作成
        Project_table='CREATE TABLE IF NOT EXISTS Project_all01(Project_name,member1,member2,member3,member4,member5)'
        Project.execute(Project_table)
        ##プロジェクト名ある？
        for datarow in Project.execute('SELECT * FROM Project_all01 where Project_name="MTKirara";'):
            if(flag==0):
                flag=1
                for i in range(5):
                    if(datarow[i]=="NULL"):
                        c=i+1
                        Project.execute('update Project_all01 set member{} = {} where Project_name="MTKirara";'.format(c,self.m_enter_v))
                        break
                    else:
                        c=c+2

        connect.commit()
        connect.close()
        ##登録確認
        if(c>5 or flag==0):
            childFrame = Error(self)
            childID = childFrame.Show()


    def showError(self,event):
        childFrame = Error(self)
        childID = childFrame.Show()



####登録画面のクラス
class TodoList(wx.Frame):
    def __init__(self,parent,id):
        ##フレーム
        wx.Frame.__init__(self,parent,id,"登録画面",size=(1400,800))
        font = wx.Font(40, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        ##パネル
        splitter = wx.SplitterWindow(self, wx.ID_ANY, style=wx.SP_LIVE_UPDATE)
        splitter.SetMinimumPaneSize(100)

        left_panel = wx.Panel(splitter, wx.ID_ANY, style=wx.BORDER_SUNKEN)
        left_panel.SetBackgroundColour(wx.WHITE)

        right_panel = wx.Panel(splitter, wx.ID_ANY, style=wx.BORDER_SUNKEN)
        right_panel.SetBackgroundColour(wx.RED)

        splitter.SplitVertically(left_panel, right_panel)
        ##テキスト
        ##左側
        self.todo_l=wx.StaticText(left_panel,-1, "やること",pos=(50,100))
        self.todo_l.SetFont(font)
        self.member_l=wx.StaticText(left_panel,-1, "メンバー",pos=(350,100))
        self.member_l.SetFont(font)
        self.ID_l=wx.StaticText(left_panel,-1, "ID",pos=(550,100))
        self.ID_l.SetFont(font)
        ##右側
        self.todo_r=wx.StaticText(right_panel,-1, 'やること',pos=(50,100))
        self.todo_r.SetFont(font)
        self.member_r=wx.StaticText(right_panel,-1, "メンバー",pos=(50,300))
        self.member_r.SetFont(font)

        ##線引き
        panel1 = wx.Panel(left_panel, pos=(0,150), size=(3000,3))
        panel1.SetBackgroundColour("BLACK")
        panel1 = wx.Panel(left_panel, pos=(300,0), size=(3,3000))
        panel1.SetBackgroundColour("BLACK")
        panel1 = wx.Panel(left_panel, pos=(540,0), size=(3,3000))
        panel1.SetBackgroundColour("BLACK")
        ##メンバー表示
        flag=0
        ##Project-allのDBと接続
        connect = sqlite3.connect('Project_all.db')
        Project= connect.cursor()
        ##テーブルの作成
        Project_table='CREATE TABLE IF NOT EXISTS Project_all01 (Project_name,member1,member2,member3,member4,member5)'
        Project.execute(Project_table)
        ##プロジェクト名ある？
        for datarow in Project.execute('SELECT * FROM Project_all01 where Project_name="MTKirara";'):
            if(flag==0):
                flag=1
                for i in range(5):
                    if(datarow[i+1]!="NULL"):
                        self.member_l[i]=wx.StaticText(left_panel,-1, datarow[i+1],pos=(50*(i+1),550))
                        self.member_l[i].SetFont(font)
                    else:
                        break
            else:
                break

        connect.commit()
        connect.close()

        ##やること入力フォーム
        self.todo_enter= wx.TextCtrl(right_panel, -1,pos=(50,200),size=(300,60))
        self.todo_enter.SetFont(font)

        ##登録ボタン
        self.button_r = wx.Button(right_panel,-1, '登録する',pos=(500,700))
        self.Bind(wx.EVT_BUTTON,self.showChild,self.button_r)
        ##メンバー登録ボタン
        self.button_m = wx.Button(right_panel,-1, 'add',pos=(50,550))
        self.Bind(wx.EVT_BUTTON,self.showChild,self.button_m)
        #チェックボックス
        #checkbox_1 = wx.CheckBox(right_panel, wx.ID_ANY, '参加',pos=(200,550))


    def showChild(self,event):
        childFrame = add_member(self)
        childID = childFrame.Show()

    def showChild2(self,event):
        childFrame2=tourokuC(self)
        childID2=childFrame2.Show()


####実装
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = TodoList(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
