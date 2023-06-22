import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import importlib
import tkinter.messagebox as mb
import sys


def switchshowpwd(password):
    if password['show'] == '':
        password['show'] = '*'
    else:
        password["show"] = ''
def switchtosms(username, root):
    global username_value, sms, exitbool
    exitbool = False
    sms = 'True'
    username_value = username.get().replace('\r','').replace('\n','').replace('\t','')
    root.destroy()

def nextpage(username, password, root):
    global username_value, password_value, sms, exitbool
    sms = 'False'
    username_value = username.get().replace('\r','').replace('\n','').replace('\t','')
    password_value = password.get().replace('\r','').replace('\n','').replace('\t','')
    if not username_value or not password_value:
        mb.showwarning("警告", "请填写用户名与密码！")
    else:
        exitbool = False
        root.destroy()

def login1(username_default=""):
    global exitbool
    exitbool = True
    root = ttk.Window(title = '乐读视频下载器-登陆', themename="morph")
    root.geometry("")
    title = ttk.Label(text = '登陆', font = ('等线 (Body Asian)', 20))
    title.grid(row = 0, column = 0)
    text1 = ttk.Label(text = '用户名(手机号或学员编号等)：')
    text1.grid(row=1)
    username = ttk.Entry(bootstyle="primary")
    username.grid(row=1,column=1)
    username.insert(0, username_default)
    smsswitch = ttk.Button(text='短信验证码登陆', bootstyle="default-outline", command=lambda: switchtosms(username, root))
    smsswitch.grid(row=1,column=2)
    text2 = ttk.Label(text = '密码：')
    text2.grid(row=2)
    password = ttk.Entry(bootstyle="primary", show="*")
    password.grid(row=2,column=1)
    showpwd = ttk.Button(text='显示/隐藏密码', bootstyle="defaulte", command=lambda: switchshowpwd(password))
    showpwd.grid(row=2,column=2)
    submit = ttk.Button(text='提交', bootstyle="primary", command=lambda: nextpage(username, password, root))
    submit.grid(row=3, column=2)
    root.mainloop()
    importlib.reload(ttk.style)
    if exitbool:
        sys.exit()
    if sms == 'False':
        return {'pwdlogin' : 'True',
            'usrname':username_value, 
            'pwd':password_value,
            }
    if sms == 'True':
        return {
            'pwdlogin' : 'False',
            'phonenum' : username_value
        }

if __name__ == '__main__':
    print(login1())