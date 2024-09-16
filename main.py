from gui.login1 import login1
from gui.login2 import login2
from gui.download1 import download1
from gui.download2 import download2
from gui.login1_sms import login1_sms
from gui.login2_sms import login2_sms
from gui.login3 import login3
import sys
import os
import webbrowser
import platform
import tkinter.messagebox as mb
import sentry_sdk

sentry_sdk.init(
    dsn="https://c25be4debe4f4a00b773850b890a4fa4@o4505250566111232.ingest.sentry.io/4505357690077184",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)


def set_global_variable(data):
    global token
    global uid
    token = data['hb_token']
    uid = str(data['pu_uid'])


def perform_login(credentials):
    if credentials['pwdlogin'] == 'True':
        return login2(credentials['usrname'], credentials['pwd'])
    smscredential = login1_sms(credentials['phonenum'])
    if smscredential['pwdlogin'] == 'False':
        return login2_sms(smscredential['phonenum'], smscredential['code'], smscredential['zonecode'])
    if smscredential['pwdlogin'] == 'True':
        return perform_login(login1(str(smscredential['phonenum'])))


def login():
    credentials = login1()
    loginresult = perform_login(credentials)
    while loginresult['success'] == 'False':
        login()
        return
    set_global_variable(loginresult['data'])
    datanext = login3(token, uid)
    if datanext['success'] == 'True':
        set_global_variable(datanext['data'])


def download():
    result, custom_down_path = download1(uid, token)
    aria2_path, aria2_config = get_aria2c_path_conf()
    for count, course in enumerate(result):
        download2(course, uid, token, aria2_path, aria2_config, custom_down_path, count + 1, len(result), platform.system()=="Windows")


def get_aria2c_path_conf():
    arch_map = {
        "amd64": "x64",
        "AMD64": "x64",
        "x86_64": "x64",
        "x64": "x64",
        "aarch64": "arm64",
        "arm64": "arm64",
    }
    os_map = {
        "Windows": "win32",
        "Linux": "linux",
        "Darwin": "darwin"
    }
    bundle_dir = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
    platform_string = os_map[platform.system()]
    arch = arch_map[platform.machine()]
    return os.path.join(bundle_dir, "bin", f"aria2c_{platform_string}_{arch}" + (".exe" if platform_string == "win32" else "")), os.path.join(bundle_dir, "bin", f"aria2_{platform_string}.conf")


try:
    login()
    download()
except Exception as e:
    sentry_sdk.capture_exception(e)
    mb.showerror('错误', '错误：' + str(e))
    alertdialog = mb.askyesno('问题反馈', '是否向作者反映该问题？')
    if alertdialog:
        mb.showinfo('问题反馈', '请在弹出的网页底部评论区中或在GitHub上提issue将错误反馈给开发者！')
        webbrowser.open("https://blog.itshenryz.com/2022/06/01/ledu-playback-download/")
    sys.exit()