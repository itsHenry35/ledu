# import the things we need
import requests
import os

def getlecturers(list, uid, token):
    url = "https://course-api-online.saasp.vdyoo.com/course/v1/student/course/user-live-list" #all the lecturers
    global courseid #used in getlecturerinfo
    global classid
    global subjectid
    global tutorid
    global lecturerid
    global name
    liveid = {}
    courseid = list['courseid']
    tutorid = list['tutorid']
    name = list['name'] #get the name of the course
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
    subjectid = json[0]['stdSubject'] #get the classid and subjectid
    lecturerid = json[0]['lecturerId'] #get the lecturer id all from the first lecturer
    count = 1
    for i in json:
        liveid [count] = i['liveId']
        count += 1
    return liveid

def getdownloadurl(id, uid, token):
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
    path = os.path.join('downloaded', name) #create a folder to store the downloaded files
    if not os.path.exists(path):
        os.makedirs(path) 
    arguments = ' -d ' + path + ' -j 64 --file-allocation=none ' + ' -o ' + filename # dir is downloads and the name, 64 thread fast downloading and filename should be changed as it is given when using aria2_download
    run = aria2c_path + ' ' + url + arguments # finally generate the command of aria2
    os.system(run) # run it!
    
def download2(list, uid, token, path__):
    global aria2c_path
    aria2c_path = path__ #get which aria2c binary to use
    id = getlecturers(list, uid, token)
    downloadurls = {}
    for i in id:
        url = getdownloadurl(str(id[i]), uid, token)
        filename = '第'+ str(i) + '讲.mp4'
        downloadurls[filename] = url
    for i in downloadurls:
        aria2_download(i, downloadurls[i])