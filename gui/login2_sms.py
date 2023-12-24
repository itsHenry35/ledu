import requests
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import importlib
import sys


def sms_verify(phone_num, sms_code, zone_code):
    url = "https://passport.100tal.com/v1/web/login/sms"
    headers = {
        'ver-num': '1.13.03',
        'content-type': 'application/x-www-form-urlencoded',
        'device-id': "TAL",
        'client-id': "523601",
        'referer': 'https://speiyou.cn/',
    }
    data = {
        'phone': phone_num,
        'sms_code': sms_code,
        'phone_code': zone_code,
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


def login2_sms(phone_num, sms_code, zone_code):
    def login_again():
        root.destroy()
        global return_data
        return_data = {
            'success': 'False'
        }

    def next_step():
        global return_data
        root.destroy()
        data = login(login_result['data'])
        return_data = {
            'success': 'True',
            'data': data,
        }

    root = ttk.Window(title='乐读视频下载器-登陆', themename="morph")
    root.geometry("")
    login_result = sms_verify(phone_num, sms_code, zone_code)
    if login_result['success']:
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
    try:
        return_data
    except:
        sys.exit()
    return return_data
