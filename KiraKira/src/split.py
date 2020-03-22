#=======================================
#構文解析 with CUI
#正則表現=>nxでDAG(有向非巡回グラフ)に変換
#=======================================
import re
from ConnectDB import ConnectDB


class Split:
    def syntax_check(self, str_in):
        str_input = str_in
        list_splited = str_input.split()      #空白で分割
        #print(list)
        word = '^[A-Z]$'        #A-Z 1文字のみ
        tip = None

        #(十分条件:root)⇨(必要条件:tip)
        list_root=[]
        flag_to = 0               #'to'が出現したかの管理 0:list_rootに追記、1：tipに記入

        for item in list_splited:
            result = re.match(word,item)
        #    print(result)
            if result:          #none以外の場合
        #        print(result.group()) 
                if (flag_to == 0):
                    list_root.append(item)
                else:
                    tip = item
                    break
            
            if  (item=='to'):   #単語が'to'の場合、flag_toを１にする
                flag_to = 1
                #行削除の記述(余裕あれば)
        
        # チェックに通らなければどちらかがない
        if len(list_root) == 0 or tip == None:
            return None
        else:
            for item in list_root:
                ConnectDB(item,tip)

        # チェックに通れば入力をそのまま返す
        return str_in

"""
str_input = input()
list_splited = str_input.split()      #空白で分割
#print(list)
word = '^[A-Z]$'        #A-Z 1文字のみ
line_num = '\d{2}'

#(十分条件:root)⇨(必要条件:tip)
list_root=[]
flag_to = 0               #'to'が出現したかの管理 0:list_rootに追記、1：tipに記入
flag_del = 0              #'del'が出現したかの管理 1:nxの処理を行わない

for item in list_splited:
    result = re.match(word,item)
    ln = re.match(line_num,item)
#    print(result)
    if result:          #none以外の場合
#        print(result.group()) 
        if (flag_to == 0):
            list_root.append(item)
        else:
            tip = item
            break
    
    if  (item=='to'):   #単語が'to'の場合、flag_toを１にする
        flag_to = 1
    if  (item=='del'):
        flag_del = 1
    if (ln and flag_del ==1):
        print('SC')
        #行削除の記述(余裕あれば)

#以下nxの処理
if (flag_del==0):
#    print(list_root)
#    print(tip)
    for item in list_root:
        ConnectDB(item,tip)
"""