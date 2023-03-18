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
        downtutorid = courselist[numlist[check_box_var1.get()]]
        downcourseid = idlist[numlist[check_box_var1.get()]]
        name = numlist[check_box_var1.get()]
        returnlist['tutorid'] = downtutorid
        returnlist['courseid'] = downcourseid
        returnlist['name'] = name
        root.destroy()
        if var.get() == 1:
            returnlist['extensiveornot'] = 'True'
        else:
            returnlist['extensiveornot'] = 'False'
    root = ttk.Window(title = '乐读视频下载器-下载', themename="morph")
    root.geometry('1280x720')
    data = getcourse(uid, token)
    count = 0
    courselist = {}
    idlist = {}
    numlist = [] #another list to storage numbers
    returnlist = {}
    var = ttk.IntVar()
    var.set(0)
    for i in data:
        courselist[i['courseName']]= i['tutorId'] #append to a dictionary
        idlist[i['courseName']]= i['stdCourseId'] #append to another dictionary
    check_box_var1 = ttk.IntVar()
    for i in courselist:
        numlist.append(i)
        radiobutton  = ttk.Radiobutton(text=i, bootstyle="primary-outline-toolbutton", variable = check_box_var1, value=count)
        radiobutton.pack(anchor = 'w')
        count +=1
    extensiveornot = ttk.Checkbutton(text='延伸课程', bootstyle="default-round-toggle", variable=var)
    extensiveornot.pack(anchor = 'w')
    submit = ttk.Button(text='提交', bootstyle="primary", command=downnextpage)
    submit.pack(anchor = 'w')
    root.mainloop()
    importlib.reload(ttk.style)
    return returnlist