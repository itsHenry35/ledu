import ctypes
import importlib
import inspect
import sys
import threading
import time
import tkinter.messagebox as mb

import requests
import ttkbootstrap as ttk


def _async_raise(tid, exctype):
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    if res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


zonelist = {
    '请选择区号': '000',
    '中国 +86': '86',
    '中国台湾 +886': '886',
    '中国澳门 +853': '853',
    '中国香港 +852': '852',
}


def after_sending(send):
    for i in range(1, 61):
        send.configure(text='重新发送(' + str(60 - i) + '秒)', state="disabled")
        time.sleep(1)
    send.configure(text='重新发送', state="enabled")


def switch_to_pwd(username, root):
    global credentials, exitbool
    exitbool = False
    credentials = {
        'pwdlogin': 'True',
        'phonenum': username.get(),
    }
    root.destroy()


def next_page(username, password, root, zonevar):
    global credentials, exitbool
    exitbool = False
    credentials = {
        'pwdlogin': 'False',
        'phonenum': username.get(),
        'code': password.get(),
        'zonecode': zonelist[zonevar.get()]
    }
    if not password.get().isdigit():
        mb.showwarning('警告', '请输入正确的验证码')
        return
    root.destroy()


def send_msg(username, zonevar, send):
    if not username.get().isdigit():
        mb.showwarning('警告', '请输入正确的手机号码')
        return
    url = "https://passport.100tal.com/v1/web/login/sms/send"
    headers = {
        "client-id": "523601",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "device-id": "TAL",
        "origin": "owcr://classroom",
        "referer": "https://speiyou.cn/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "ver-num": "1.13.03"
    }
    data = {
        'verify_type': 1,
        'phone': username.get(),
        'phone_code': zonelist[zonevar.get()]
    }
    data1 = requests.post(url, data=data, headers=headers)
    json = data1.json()
    mb.showinfo('提示', json['errmsg'])
    thread_ = 1
    if json['errcode'] == 0:
        global thread
        thread = threading.Thread(target=after_sending, args=(send,))
        thread.start()
    return thread_


def login1_sms(phonenum):
    global root, exitbool
    exitbool = True
    phonenum = str(phonenum)
    thread_ = 0
    root = ttk.Window(title='乐读视频下载器-登录', themename="morph")
    root.geometry("")
    title = ttk.Label(text='登录', font=('等线 (Body Asian)', 20))
    title.grid(row=0, column=0)
    text1 = ttk.Label(text='手机号：')
    text1.grid(row=1)
    username = ttk.Entry(bootstyle="primary")
    username.grid(row=1, column=2)
    username.insert(0, phonenum)
    zonevar = ttk.StringVar()
    zonevar.set("请选择区号")
    zone = ttk.OptionMenu(root, zonevar, *zonelist)
    zone.grid(row=1, column=1)
    smsswitch = ttk.Button(text='返回账号密码登录', bootstyle="default-outline",
                           command=lambda: switch_to_pwd(username, root))
    smsswitch.grid(row=1, column=3)
    text2 = ttk.Label(text='验证码：')
    text2.grid(row=2)
    password = ttk.Entry(bootstyle="primary")
    password.grid(row=2, column=2)
    send = ttk.Button(text='发送验证码', bootstyle="default",
                      command=lambda: send_msg(username, zonevar, send))
    send.grid(row=2, column=3)
    submit = ttk.Button(text='提交', bootstyle="primary", command=lambda: next_page(username, password, root, zonevar))
    submit.grid(row=3, column=3)
    root.mainloop()
    if thread_ == 1:
        stop_thread(thread)
    importlib.reload(ttk.style)
    if exitbool:
        sys.exit()
    return credentials
