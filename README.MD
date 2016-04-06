http_basic_auth_passwd_scanner.py
=======================================
a simple multi-thread http_basic_auth_passwd_scanner 

how to use 
---------------
1,the scanner use requests ,so if it not in your system install it
'''
    pip install requests
    '''
2,modily the config.py
'''
    #set Number of concurrent threads
    threadsNo = 5
    #set the scan url
    url = 'http://192.168.1.1'
    #set username list,must be a list
    usernameList = ['admin','root','administrator']
    #set retry geturl times 
    trytimes= 3
    #set every scan sleep time
    sleep_time=0.02
'''
3,if you have a big password_dict cover passwddict.txt

4,run it
'''
    python http_basic_auth_passwd_scanner.py
    '''
    

    
in chinese
-----------------
多线程路由器或是服务器基础验证密码探测工具
============================================

使用方法
-------------
1,程序用到了rqeuests模块,如果你系统里没有,需要安装
'''
    pip install requests
    '''
2,更改配置文件config.py
'''
     #set Number of concurrent threads 设置线程数,不建议大于10
    threadsNo = 5
    #set the scan url      设置服务器或路由地址
    url = 'http://192.168.1.1'
    #set username list,must be a list 设置用户名列表
    usernameList = ['admin','root','administrator']
    #set retry geturl times     设置连接url出现错误时间重试次数
    trytimes= 3
    #set every scan sleep time   设置每次探测时间
    sleep_time=0.02
    '''
3,找个大的字典替换字典文件 password_dict.txt

4,运行
'''
    python http_basic_auth_passwd_scanner.py
    '''

