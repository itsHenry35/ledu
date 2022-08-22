from gui.login1 import login1
from gui.login2 import login2
from gui.download1 import download1
from gui.download2 import download2
import sys, os
import platform
    
def set_alldata(data):
    global token
    global uid
    token = data['hb_token']
    uid = str(data['pu_uid'])
    

def login():
    credentials = login1()
    loginresult = login2(credentials['usrname'], credentials['pwd'])
    if loginresult['success'] == 'False':
        login()
    if loginresult['success'] == 'True':
        set_alldata(loginresult['data'])

def download():
    result = download1(uid, token)
    path__ = get_platform_info()
    download2(result, uid, token, path__)

def get_platform_info():
    if getattr(sys, 'frozen', False): # we are running in a bundle
        bundle_dir = sys._MEIPASS # This is where the files are unpacked to
    else: # normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    platform_ = platform.system()
    if platform_ == 'Windows':
        aria2c_path = bundle_dir + '\\bin\\aria2c_win.exe'
    elif platform_ == 'Linux':
        if platform.machine == 'x86_64':
            aria2c_path = './bin/aria2c_linux_amd64'
        if platform.machine == 'armv8' or platform.machine == 'armv8l':
            aria2c_path = './bin/aria2c_linux_arm64'
    elif platform_ == 'Darwin':
        aria2c_path = './bin/aria2c_macos'
    else:
        print('暂不支持的系统！请使用Windows、Linux、MacOSX或Android系统(测试中)！') #if the system is not supported, print out(ios and unknown kernels are not supported yet)
        print('你的系统是：' + platform_)
        input("") #let users see the message
        sys.exit()
    return aria2c_path

login()
download()