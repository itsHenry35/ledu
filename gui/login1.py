import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import importlib

def login1():
    def switchshowpwd():
        if password['show'] == '':
            password['show'] = '*'
        else:
            password["show"] = ''
    def nextpage():
        global username_
        global password_
        username_ = username.get()
        password_ = password.get()
        root.destroy()
    root = ttk.Window(title = '乐读视频下载器-登陆', themename="morph")
    root.geometry('1280x720')
    title = ttk.Label(text = '登陆', font = ('等线 (Body Asian)', 20))
    title.grid(row = 0, column = 0)
    text1 = ttk.Label(text = '用户名(手机号或学员编号等)：')
    text1.grid(row=1)
    username = ttk.Entry(bootstyle="primary")
    username.grid(row=1,column=1)
    text2 = ttk.Label(text = '密码：')
    text2.grid(row=2)
    password = ttk.Entry(bootstyle="primary", show="*")
    password.grid(row=2,column=1)
    showpwd = ttk.Button(text='显示/隐藏密码', bootstyle="default-outline", command=switchshowpwd)
    showpwd.grid(row=2,column=2)
    submit = ttk.Button(text='提交', bootstyle="primary", command=nextpage)
    submit.grid(row=3, column=1)
    root.mainloop()
    importlib.reload(ttk.style)
    return {'usrname':username_, 
        'pwd':password_,
        }