import requests
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import importlib
import sys


def pwd_verify(user, password):
    url = "https://passport.100tal.com/v1/web/login/pwd"
    headers = {
        'ver-num': '1.13.03',
        'content-type': 'application/x-www-form-urlencoded',
        'device-id': "TAL",
        'client-id': "523601",
        'referer': 'https://speiyou.cn/',
    }
    data = {
        'symbol': user,
        'password': password,
        'source_type': 2,
        'domain': 'xueersi.com',
    }
    response = requests.post(url, data=data, headers=headers)
    json_response = response.json()
    if json_response['errcode'] == 0:
        return {'success': True,
                'data': json_response['data'],
                'msg': json_response['errmsg']
                }
    return {'success': False,
            'msg': json_response['errmsg']
            }


def login(data):
    url = "https://course-api-online.saasp.vdyoo.com/passport/v1/login/student/code"
    code = data['code']
    headers = {
        "Referer": "https://speiyou.cn/",
    }

    data = {"code": code,
            "deviceId": "TAL",
            "terminal": "pc",
            "product": "ss",
            "clientId": "523601"
            }

    response = requests.post(url, json=data, headers=headers)
    json_response = response.json()
    return json_response


def login2(username, password):
    def login_again():
        global result_submit, exitbool
        exitbool = False
        root.destroy()
        result_submit = {
            'success': False
        }

    def next_step():
        global result_submit, exitbool
        exitbool = False
        root.destroy()
        data = login(login_result['data'])
        result_submit = {
            'success': True,
            'data': data,
        }

    global exitbool
    exitbool = True
    root = ttk.Window(title='乐读视频下载器-登陆', themename="morph")
    root.geometry("")
    login_result = pwd_verify(username, password)
    if login_result['success'] is True:
        text1 = ttk.Label(text=login_result['msg'])
        text1.grid(row=1)
        submit = ttk.Button(text='下一步', bootstyle="primary", command=next_step)
        submit.grid(row=2)
    else:
        text1 = ttk.Label(text=login_result['msg'])
        text1.grid(row=1)
        submit = ttk.Button(text='重试', bootstyle="primary", command=login_again)
        submit.grid(row=2)
    root.mainloop()
    importlib.reload(ttk.style)
    if exitbool:
        sys.exit()
    return result_submit
