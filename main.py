from gui.login1 import login1
from gui.login2 import login2
from gui.download1 import download1
from gui.download2 import download2
    
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
    download2(result, uid, token)

login()
download()