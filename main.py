# import the things we need
import requests
import sys
import os
import yaml

def config(): #read config
    global user
    global password
    configfile = open('config.yaml', 'r', encoding="utf-8")
    data = yaml.load(configfile,Loader=yaml.FullLoader)
    user = data['username']
    password = data['password']

def pwdverify():
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
    print (json['errmsg'])
    if json['errcode'] == 0: # no error, then login
        return json['data']
    else:
        sys.exit() # error, after printing error msg, quit the program


def login():
    url = "https://course-api-online.saasp.vdyoo.com/passport/v1/login/student/code" # login api
    data = pwdverify()
    token = data['passport_token']
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

def getcourse():
    url = "https://course-api-online.saasp.vdyoo.com/course/v1/student/course/list" # get_course_url_basic
    headers =  {
        "Host": "course-api-online.saasp.vdyoo.com",
        "stuId": uid,
        "resVer": "1.0.6",
        "terminal": "pc",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "expireTime": "0",
        "branchId": "",
        "token": token,
        "version": "3.21.0.84",
        "Referer": "https://speiyou.cn/",
    }
    adddata = '?stuId='+ uid+ '&courseStatus=0&stdSubject=&page=1&perPage=500&order=asc' #i've no idea why adding this to data won't work, so I add it directly to the URL
    url = url + adddata
    data1 = requests.get(url, headers = headers) # submit the data to get global token
    return data1.json() # return courses


def userchoosetutorid(): # let users to choose what to download
    global name
    data = getcourse()
    count = 1
    courselist = {}
    idlist = {}
    numlist = {} #another list to storage numbers
    returnlist = {}
    for i in data:
        courselist[i['courseName']]= i['tutorId'] #append to a dictionary
        idlist[i['courseName']]= i['stdCourseId'] #append to another dictionary
    count = 1 # need a count
    for i in courselist:
        print(str(count) + ' ' + i) #print a count with a name that users can choose easily
        numlist[str(count)]= i
        count +=1
    num = input('请输入你想要下载的课程的编号\n')
    if num in numlist:
        downtutorid = courselist[numlist[num]]
        downcourseid = idlist[numlist[num]]
        name = numlist[num]
        returnlist['tutorid'] = downtutorid
        returnlist['courseid'] = downcourseid
        return returnlist
    else:
        print('课程编号不存在！')
        returnlist = userchoosetutorid()
        return returnlist

def getlecturers():
    url = "https://course-api-online.saasp.vdyoo.com/course/v1/student/course/user-live-list" #all the lecturers
    list = userchoosetutorid()
    global courseid
    global classid
    global subjectid
    global tutorid
    global lecturerid
    liveid = {}
    courseid = list['courseid']
    tutorid = list['tutorid']
    adddata = '?stuId='+ uid + '&stdCourseId=' + courseid + '&type=1&needPage=1&page=1&perPage=500&order=asc'
    url = url + adddata
    headers = {
        "Host": "course-api-online.saasp.vdyoo.com",
        "stuId": uid,
        "resVer": "1.0.6",
        "terminal": "pc",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "token": token,
        "version": "3.21.0.84",
        "Referer": "https://speiyou.cn/",
    }
    data = requests.get(url, headers = headers) # get lecturers
    json = data.json()
    classid = json[0]['stdClassId']
    subjectid = json[0]['stdSubject']
    lecturerid = json[0]['lecturerId']
    count = 1
    for i in json:
        liveid [count] = i['liveId']
        count += 1
    return liveid

def getdownloadurl(id):
    url = 'https://classroom-api-online.saasp.vdyoo.com/playback/v1/video/init'
    headers = {
        "Host": "classroom-api-online.saasp.vdyoo.com",
        "stuId": uid,
        "appClientType": "xes",
        "lecturerId": lecturerid,
        "stdSubject": subjectid,
        "tutorId": tutorid,
        "stdCourseId": courseid,
        "resVer": "1.0.6",
        "liveId": id,
        "terminal": "pc",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "stdClassId": classid,
        "expireTime": "0",
        "token": token,
        "version": "3.21.0.84",
        "Referer": "https://speiyou.cn/",
    }
    data = requests.get(url, headers = headers) # get one lecturer info
    json = data.json()
    videourl = json['videoUrls'][2] # get the download url of mp4 from the info
    return videourl


def aria2_download(filename, url):
    path = 'downloaded\\' + name
    if not os.path.exists(path):  # create the downloaded folder
        os.makedirs(path) 
    arguments = ' -d ' + path + ' -j 64 --file-allocation=none ' + ' -o ' + filename # dir is downloads and the name, 64 thread fast downloading and filename should be changed as it is given when using aria2_download
    run = 'aria2c.exe ' + url + arguments # finally generate the command of aria2
    os.system(run) # run it!
    
def download():
    id = getlecturers()
    downloadurls = {}
    for i in id:
        url = getdownloadurl(str(id[i]))
        filename = '第'+ str(i) + '讲.mp4'
        downloadurls[filename] = url
    for i in downloadurls:
        aria2_download(i, downloadurls[i])
    
    

config() #run everything at last
logindata = login() # fetch the global data
token = logindata['hb_token']
uid = str(logindata['pu_uid'])
download()