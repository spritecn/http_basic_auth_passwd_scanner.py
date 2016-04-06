#coding:utf8
#
#HTTP BASIC Auth PASSWD SCANNER's ConfigFile
#AUTHOR:SpriteCN
#BLOG:http://www.fantansy.cn
#

#set Number of concurrent threads
threadsNo = 5
#set the scan url
url = 'http://192.168.1.1/'
#set username list,must be a list
usernameList = ['admin','root','administrator']
#set retry geturl times 
trytimes= 3
#set every scan sleep time(s)
sleep_time=0.03