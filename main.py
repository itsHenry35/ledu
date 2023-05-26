from gui.login1 import login1
from gui.login2 import login2
from gui.download1 import download1
from gui.download2 import download2
from gui.login1_sms import login1_sms
from gui.login2_sms import login2_sms
from gui.login3 import login3
import sys, os
import platform
import tkinter.messagebox as mb
import requests

def set_alldata(data):
    global token
    global uid
    token = data['hb_token']
    uid = str(data['pu_uid'])

def perform_login(credentials):
    if credentials['success'] == 'True':
        return login2(credentials['usrname'], credentials['pwd'])
    else:
        smscredential = login1_sms(credentials['phonenum'])
        if smscredential['success'] == 'True':
            return login2_sms(credentials['phonenum'], smscredential['code'], smscredential['zonecode'])
        if smscredential['success'] == 'False':
            return login()

def login():
    credentials = login1()
    loginresult = perform_login(credentials)
    while loginresult['success'] == 'False':
        loginresult = login()

    set_alldata(loginresult['data'])
    datanext = login3(token, uid)
    if datanext['success'] == 'True':
        set_alldata(datanext['data'])

def download():
    result = download1(uid, token)
    path__ = get_platform_info()
    download2(result, uid, token, path__)

def get_platform_info():
    bundle_dir = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
    platform_ = platform.system()
    aria2c_path = ""

    if platform_ == 'Windows':
        aria2c_path = bundle_dir + '\\bin\\aria2c_win.exe'
    elif platform_ == 'Linux':
        if platform.machine == 'x86_64':
            aria2c_path = bundle_dir + '/bin/aria2c_linux_amd64'
        if platform.machine == 'armv8' or platform.machine == 'armv8l':
            aria2c_path = bundle_dir + '/bin/aria2c_linux_arm64'
    elif platform_ == 'Darwin':
        aria2c_path = bundle_dir + '/bin/aria2c_macos'
    else:
        raise Exception(f'暂不支持的系统！请使用Windows、Linux、MacOSX或Android系统(测试中)！你的系统是：{platform_}')

    return aria2c_path

try:
    login()
    download()
except Exception as e:
    mb.showerror('错误：' + str(e))
    sys.exit(1)