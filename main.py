from gui.login1 import login1
from gui.login2 import login2
from gui.download1 import download1
from gui.download2 import download2
from gui.login1_sms import login1_sms
from gui.login2_sms import login2_sms
from gui.login3 import login3
import sys, os, webbrowser
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
    else:
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
    aria2_path = get_platform_info()
    for count, course in enumerate(result):
        download2(course, uid, token, aria2_path, custom_down_path, count + 1, len(result))


def get_platform_info():
    bundle_dir = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
    platform_ = platform.system()
    aria2c_path = ""

    if platform_ == 'Windows':
        aria2c_path = f"\"{bundle_dir}\\bin\\aria2c_win.exe\""
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
    sentry_sdk.capture_exception(e)
    mb.showerror('错误', '错误：' + str(e))
    alertdialog = mb.askyesno('错误反馈', '是否打开错误反馈页面？')
    if alertdialog:
        mb.showinfo('错误反馈', '请在弹出的网页底部评论区中或在GitHub上将错误反馈给开发者！')
        webbrowser.open("https://blog.itshenryz.com/2022/06/01/ledu-playback-download/")
    sys.exit()
