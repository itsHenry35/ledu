import requests
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import importlib
import sys


def get_account_list(token, uid):
    url = "https://course-api-online.saasp.vdyoo.com/passport/v1/students/account-list"
    headers = {
        "Content-Type": "application/json",
        "Origin": "owcr://classroom",
        "Referer": "https://speiyou.cn/",
        "resVer": "1.0.6",
        "terminal": "pc",
        "token": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "version": "3.22.0.99"
    }
    data = {
        "stuPuId": uid,
        "signToken": token
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


def login3(token, uid_now):
    global final_account

    def get():
        global final_account
        final_account = account_list[var.get()]

    def submit():
        global final_account
        global result
        result = {
            'success': True
        }
        if final_account['isCurrentLoginAccount']:
            result["success"] = False
        else:
            uidnext = final_account['pu_uid']
            result_switch = switch_account(uid_now, uidnext, token)
            result['data'] = result_switch
        root.destroy()

    count = 0
    root = ttk.Window(title='乐读视频下载器-登陆', themename="morph")
    root.geometry("")
    text0 = ttk.Label(text='请选择学员')
    text0.grid(row=0)
    account_list = get_account_list(token, uid_now)
    final_account = account_list[0]
    var = ttk.IntVar()
    var.set(0)
    for i in account_list:
        account = ttk.Radiobutton(root, text=i['nickname'], variable=var, value=count, command=get)
        account.grid(row=count + 1, column=0)
        count += 1
    button = ttk.Button(text='提交', bootstyle="primary", command=submit)
    button.grid(row=count + 1, column=0)
    root.mainloop()
    importlib.reload(ttk.style)
    try:
        result
    except:
        sys.exit()
    return result


def switch_account(current_uid, next_uid, token):
    url = "https://course-api-online.saasp.vdyoo.com/passport/v2/login/student/change-stu"
    headers = {
        "Content-Type": "application/json",
        "terminal": "pc",
        "token": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "version": "3.22.0.99"
    }
    data = {
        "stuPuId": next_uid,
        "currentStuPuId": current_uid,
        "signToken": token
    }
    return requests.post(url=url, headers=headers, json=data).json()
