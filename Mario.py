import ctypes
import os
import platform
import threading
from uuid import uuid4
import time
from subprocess import call
import colorama
import pwinput
import requests
from colorama import Fore

if platform.system() == "Windows":
    clear = "cls"
    os.system(clear)
else:
    clear = "clear"

phone_num = None
email = None
target = None
usernamep = None
passwd = None
logged_in = False
csrf_token = "HQJVhHvZ4uOQYfA8h1Cu0tT1McGk6lqo"
api1 = 'https://i.instagram.com/api/v1/accounts/login/'
api2 = 'https://instagram.com/accounts/edit'
option = 1
uid = uuid4()
call("mode 67,10",shell=True)
print(F'[' +Fore.WHITE + Fore.GREEN+ '+' +Fore.GREEN + Fore.WHITE +']'+' Mario Target Turbo | Version 1.0 By zrx')
print()

if option == 1:
    def login(usernamep,passwd):
        headers = {
            'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
            "Accept": "/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US",
            "X-IG-Capabilities": "3brTvw==",
            "X-IG-Connection-Type": "WIFI",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Host': 'i.instagram.com',
            'Connection': 'keep-alive'
            }
        data = {
            'uuid': uid,
            'password': passwd,
            'username': usernamep,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'YcJzPesTYxMTfmpSOiVn3pfRAJdrETFD',
            'login_attempt_countn': '0'
        }
        r = requests.post(api1,headers=headers,data=data)

        if "logged_in_user" in r.text:
            print(F'[' +Fore.WHITE + Fore.GREEN+ '+' +Fore.GREEN + Fore.WHITE +']'+' Successfully logged in')
            print()
            my_cookies = r.cookies
            for cookie in my_cookies:
                if cookie.name == 'mid':
                    mid = cookie.value
                if cookie.name == "ds_user_id":
                    ds_user_id = cookie.value
                if cookie.name == "csrftoken":
                    csrf = cookie.value
                if cookie.name == "sessionid":
                    sessionid = cookie.value
            cookie = "csrftoken=" + csrf + ";mid=" + mid + ";ds_user_id=" + ds_user_id + ";sessionid=" + sessionid
            print(cookie)

            getheaders = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Cookie": "" + cookie + "",
            }
            
        else:
            print(Fore.RED + '[!]' + Fore.BLUE + f' Password is incorrect / Other details are not valid. try again')
            time.sleep(15)
    usernamep = str(input(F'[' +Fore.WHITE + Fore.YELLOW+ '?' +Fore.YELLOW + Fore.WHITE +']'+' Username: '))
    print()
    passwd = pwinput.pwinput(prompt=str(F'[' +Fore.WHITE + Fore.YELLOW+ '?' +Fore.YELLOW + Fore.WHITE +']'+' Password: '), mask='*')
    print(F'[' +Fore.WHITE + Fore.MAGENTA+ '*' +Fore.MAGENTA + Fore.WHITE +']'+' Attempting to login...')
    print()
    login(usernamep, passwd)

