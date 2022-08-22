import requests
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import importlib

def pwdverify(user, password):
    url= "https://passport.100tal.com/v1/web/login/pwd" #password verify api

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
    'domain' : 'xueersi.com',
    }

    data1 = requests.post(url,data=data, headers = headers) # submit the data to get login token
    json = data1.json()
    if json['errcode'] == 0: # no error, then try login
        return {'success' : 'True',
            'data' : json['data'],
            'msg' : json['errmsg']
            }
    else:
        return {'success' : 'False',
            'msg' : json['errmsg']
            }

def login(data):
    url = "https://course-api-online.saasp.vdyoo.com/passport/v1/login/student/code" # login api
    code = data['code']
    headers = {
    "Referer": "https://speiyou.cn/",
    }

    data = {"code":code,
    "deviceId":"TAL",
    "terminal":"pc",
    "product":"ss",
    "clientId":"523601"
    }

    data1 = requests.post(url,json=data, headers = headers) # submit the data to get global token
    json = data1.json() # convert to json so can be accessed
    return json

def login2(username, password):
    def loginagain():
        root.destroy()
        global result_
        result_ =  {
            'success' : 'False'
        }
    def nextstep():
        global result_
        root.destroy()
        data = login(loginresult['data'])
        result_ = {
            'success' : 'True',
            'data' : data,
        }
    root = ttk.Window(title = '乐读视频下载器-登陆', themename="morph")
    root.geometry('1280x720')
    loginresult = pwdverify(username, password)
    if loginresult['success'] == 'True':
        text1 = ttk.Label(text = loginresult['msg'])
        text1.grid(row=1)
        submit = ttk.Button(text='下一步', bootstyle="primary", command=nextstep)
        submit.grid(row=2)
    else:
        text1 = ttk.Label(text = loginresult['msg'])
        text1.grid(row=1)
        submit = ttk.Button(text='重试', bootstyle="primary", command=loginagain)
        submit.grid(row=2)
    root.mainloop()
    importlib.reload(ttk.style)
    return result_