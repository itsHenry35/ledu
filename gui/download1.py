import requests
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import importlib
def getcourse(uid, token):
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


def download1(uid, token):
    def downnextpage():
        for i in widgetlist:
            downtutorid = courselist[numlist[i]]
            downcourseid = idlist[numlist[i]]
            name = numlist[i]
            returnlist['tutorid'] = downtutorid
            returnlist['courseid'] = downcourseid
            returnlist['name'] = name
        root.destroy()
    root = ttk.Window(title = '乐读视频下载器-下载', themename="morph")
    root.geometry('1280x720')
    data = getcourse(uid, token)
    count = 1
    courselist = {}
    idlist = {}
    numlist = {} #another list to storage numbers
    returnlist = {}
    widgetlist = {}
    for i in data:
        courselist[i['courseName']]= i['tutorId'] #append to a dictionary
        idlist[i['courseName']]= i['stdCourseId'] #append to another dictionary
    for i in courselist:
        numlist[str(count)]= i
        checkbutton  = ttk.Checkbutton(text=i, bootstyle="default-round-toggle")
        checkbutton.grid(row = count-1, column = 0)
        widgetlist[str(count)] = checkbutton
        count +=1
    submit = ttk.Button(text='提交', bootstyle="primary", command=downnextpage)
    submit.grid (row = count, column = 0)
    root.mainloop()
    return returnlist