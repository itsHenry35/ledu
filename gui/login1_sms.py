import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import importlib
import requests
import time
import threading

import inspect
 
import ctypes
 
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
 
        raise SystemError("PyThreadState_SetAsyncExc failed")
 
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


zonelist = {
 '请选择区号' : '000',
 '中国 +86': '86',
 '中国台湾 +886': '886',
 '中国澳门 +853': '853',
 '中国香港 +852': '852',
}

def login1_sms(phonenum):
    global root
    def after_sending():
        for i in range(1,61):
            send.configure(text='重新发送(' + str(60-i) + '秒)', state="disabled")
            time.sleep(1)
        send.configure(text='重新发送', state="enabled")
    phonenum = str(phonenum)
    def switchtopwd():
        global ispwd
        root.destroy()
        ispwd = 'True'
    def nextpage():
        global phonenum_
        global smscode_
        global ispwd
        phonenum_ = username.get()
        smscode_ = password.get()
        root.destroy()
        ispwd = 'False'
    def sendmsg():
        global thread
        global thread_
        url= "https://passport.100tal.com/v1/web/login/sms/send" #sms send api
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
        data1 = requests.post(url,data=data, headers = headers) # submit the data to get send sms
        json = data1.json()
        ttk.dialogs.dialogs.Messagebox.ok(json['errmsg'], title='提示', alert=True, parent=None, )
        thread_ = 1
        if json['errcode'] == 0:
            thread = threading.Thread(target=after_sending)
            thread.start()
    thread_ = 0
    root = ttk.Window(title = '乐读视频下载器-登陆', themename="morph")
    root.geometry('1280x720')
    title = ttk.Label(text = '登陆', font = ('等线 (Body Asian)', 20))
    title.grid(row = 0, column = 0)
    text1 = ttk.Label(text = '手机号：')
    text1.grid(row=1)
    username = ttk.Entry(bootstyle="primary")
    username.grid(row=1,column=2)
    username.insert(0,phonenum)
    zonevar = ttk.StringVar()
    zonevar.set("请选择区号")
    zone = ttk.OptionMenu(root,  zonevar, *zonelist)
    zone.grid (row=1,column=1)
    text2 = ttk.Label(text = '验证码：')
    text2.grid(row=2)
    password = ttk.Entry(bootstyle="primary")
    password.grid(row=2,column=2)
    send = ttk.Button(text='发送验证码', bootstyle="default", command=sendmsg)
    send.grid(row=2,column=3)
    smsswitch = ttk.Button(text='返回账号密码登陆', bootstyle="default-outline", command=switchtopwd)
    smsswitch.grid(row=2,column=4)
    submit = ttk.Button(text='提交', bootstyle="primary", command=nextpage)
    submit.grid(row=3, column=3)
    root.mainloop()
    if thread_ == 1:
        stop_thread(thread)
    importlib.reload(ttk.style)
    print(ispwd)
    if ispwd == 'False':
        return {'success' : 'True',
            'phonenum':phonenum_, 
            'code': smscode_,
            'zonecode' : zonelist[zonevar.get()]
            }
    if ispwd == 'True':
        return {'success' : 'False',}